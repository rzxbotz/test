from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Admin Channel ID where feedback is sent
ADMIN_CHANNEL_ID = -1001906863982  # Replace with your actual channel ID

# Dictionary to store user feedback message mapping
feedback_users = {}

@Client.on_message(filters.private & filters.command("feedback"))
async def ask_feedback(client, message):
    """ Ask users for feedback confirmation before submission """
    user_id = message.chat.id
    user_message = message.text.split(" ", 1)

    if len(user_message) < 2:
        await message.reply_text("Example: `/feedback This bot is amazing!`")
        return

    feedback_text = user_message[1]

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Submit Feedback", callback_data=f"submit_feedback|{user_id}")],
        [InlineKeyboardButton("❌ Cancel", callback_data="cancel_feedback")]
    ])

    await message.reply_text(
        f"📝 **Your Feedback:**\n\n{feedback_text}\n\nDo you want to submit it?",
        reply_markup=keyboard
    )

@Client.on_callback_query(filters.regex(r"submit_feedback\|(\d+)"))
async def submit_feedback(client, query):
    """ Handles feedback submission after user confirmation """
    user_id = int(query.data.split("|")[1])
    message = query.message

    if message.reply_to_message:
        feedback_text = message.reply_to_message.text
    else:
        await query.answer("❌ Error: No feedback found.")
        return

    user = await client.get_users(user_id)
    user_name = user.first_name

    sent_feedback = await client.send_message(
        ADMIN_CHANNEL_ID,
        f"📩 **New Feedback Received**\n\n👤 **User:** [{user_name}](tg://user?id={user_id})\n🆔 **User ID:** `{user_id}`\n\n💬 **Message:**\n{feedback_text}\n\n🔹 *Reply to this message to respond anonymously.*"
    )

    feedback_users[sent_feedback.message_id] = user_id

    await query.message.edit_text("✅ Your feedback has been submitted successfully! Thank you.")

@Client.on_callback_query(filters.regex(r"cancel_feedback"))
async def cancel_feedback(client, query):
    """ Handles feedback cancellation """
    await query.message.edit_text("❌ Feedback submission canceled.")

@Client.on_message(filters.channel & filters.reply)
async def reply_to_feedback(client, message: Message):
    """ Admin replies are sent anonymously via the bot """
    replied_message = message.reply_to_message

    if not replied_message or replied_message.message_id not in feedback_users:
        return  # Ignore if it's not a reply to a feedback message

    user_id = feedback_users[replied_message.message_id]
    admin_reply = message.text

    try:
        await client.send_message(
            user_id,
            f"📩 **Admin Reply:**\n\n{admin_reply}\n\n🔹 *This is an automated response.*"
        )
        await message.reply_text("✅ Reply sent anonymously to the user.")
    except Exception as e:
        await message.reply_text("❌ Failed to send reply. The user may have blocked the bot.")
        print(f"Error sending reply: {e}")
  
