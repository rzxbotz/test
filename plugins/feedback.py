import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# ✅ Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Your Admin Channel ID (Replace with the correct one)
ADMIN_CHANNEL_ID = -1001906863982  

# Store user feedback temporarily
pending_feedback = {}

@Client.on_message(filters.private & filters.command("feedback"))
async def ask_feedback(client, message: Message):
    """ Ask users for feedback confirmation before submission """
    try:
        user_id = message.chat.id
        user_message = message.text.split(" ", 1)

        if len(user_message) < 2:
            await message.reply_text("❌ Please provide feedback. Example: `/feedback This bot is amazing!`")
            return

        feedback_text = user_message[1]
        pending_feedback[user_id] = feedback_text  

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ Submit Feedback", callback_data=f"submit_feedback|{user_id}")],
            [InlineKeyboardButton("❌ Cancel", callback_data=f"cancel_feedback|{user_id}")]
        ])

        await message.reply_text(
            f"📝 **Your Feedback:**\n\n{feedback_text}\n\nDo you want to submit it?",
            reply_markup=keyboard
        )
    except Exception as e:
        logger.error(f"Error in ask_feedback: {e}")

@Client.on_callback_query(filters.regex(r"submit_feedback\|(\d+)"))
async def submit_feedback(client, query: CallbackQuery):
    """ Handles feedback submission after user confirmation """
    try:
        user_id = int(query.data.split("|")[1])

        if user_id not in pending_feedback:
            await query.answer("❌ No feedback found.", show_alert=True)
            return

        feedback_text = pending_feedback.pop(user_id)

        user = await client.get_users(user_id)
        user_name = user.first_name

        await client.send_message(
            ADMIN_CHANNEL_ID,
            f"📩 **New Feedback Received**\n\n👤 **User:** [{user_name}](tg://user?id={user_id})\n🆔 **User ID:** `{user_id}`\n\n💬 **Message:**\n{feedback_text}\n\n🔹 *Reply to this message to respond anonymously.*"
        )

        await query.answer("✅ Feedback submitted!", show_alert=True)
        await query.message.edit_text("✅ Your feedback has been submitted successfully! Thank you.")
    except Exception as e:
        logger.error(f"Error in submit_feedback: {e}")

@Client.on_callback_query(filters.regex(r"cancel_feedback\|(\d+)"))
async def cancel_feedback(client, query: CallbackQuery):
    """ Handles feedback cancellation """
    try:
        user_id = int(query.data.split("|")[1])

        if user_id in pending_feedback:
            pending_feedback.pop(user_id)

        await query.answer("❌ Feedback submission canceled.", show_alert=True)
        await query.message.edit_text("❌ Feedback submission canceled.")
    except Exception as e:
        logger.error(f"Error in cancel_feedback: {e}")

@Client.on_message(filters.channel & filters.reply)
async def reply_to_feedback(client, message: Message):
    """ Admin replies are sent anonymously via the bot """
    try:
        replied_message = message.reply_to_message

        if not replied_message:
            return  

        # Extract User ID from the feedback message
        user_id = None
        for line in replied_message.text.split("\n"):
            if line.startswith("🆔 **User ID:**"):
                user_id = int(line.split("`")[1])
                break

        if not user_id:
            return  

        admin_reply = message.text

        try:
            await client.send_message(
                user_id,
                f"📩 **Admin Reply:**\n\n{admin_reply}\n\n🔹 *This is an automated response.*"
            )
            await message.reply_text("✅ Reply sent anonymously to the user.")
        except Exception as e:
            logger.error(f"Error sending reply to user {user_id}: {e}")
            await message.reply_text("❌ Failed to send reply. The user may have blocked the bot.")
    except Exception as e:
        logger.error(f"Error in reply_to_feedback: {e}")
        
