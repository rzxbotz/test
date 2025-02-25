import logging
from pyrogram import Client, filters
from pyrogram.types import Message

# ✅ Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Admin Channel ID (Replace with the correct one)
ADMIN_CHANNEL_ID = -1001906863982  

@Client.on_message(filters.private & filters.command("feedback"))
async def submit_feedback(client, message: Message):
    """ Immediately submits feedback to the admin channel """
    try:
        user_id = message.chat.id
        user_message = message.text.split(" ", 1)

        if len(user_message) < 2:
            await message.reply_text("❌ Please provide feedback. Example: `/feedback This bot is amazing!`")
            return

        feedback_text = user_message[1]
        user = await client.get_users(user_id)
        user_name = user.first_name
        mention = f'<a href="tg://user?id={user_id}">{user_name}</a>'

        # Send feedback to the admin channel
        sent_message = await client.send_message(
            ADMIN_CHANNEL_ID,
            f"<b>📩 New Feedback Received</b>\n\n"
            f"<b>💬 Message:</b>\n{feedback_text}\n\n"
            f"<b>👤 User:</b> {mention}\n"
            f"<b>🆔 User ID:</b> `{user_id}`",
            parse_mode="html"
        )

        # Store the original feedback message ID for reference
        sent_message.reply_markup = None  # Remove reply markup to avoid confusion

        await message.reply_text("✅ Your feedback has been submitted successfully! Thank you.")
    
    except Exception as e:
        logger.error(f"Error in submit_feedback: {e}")
        await message.reply_text("❌ An error occurred while submitting your feedback. Please try again later.")

@Client.on_message(filters.channel & filters.reply)
async def reply_to_feedback(client, message: Message):
    """ Admin replies are sent anonymously via the bot """
    try:
        replied_message = message.reply_to_message

        if not replied_message:
            return  

        # Extract User ID from the feedback message
        user_id = None
        feedback_text = None

        for line in replied_message.text.split("\n"):
            if "🆔 User ID:" in line:
                user_id = int(line.split("`")[1])
            elif "💬 Message:" in line:
                feedback_text = replied_message.text.split("💬 Message:")[1].strip()

        if not user_id:
            return  

        admin_reply = message.text

        try:
            await client.send_message(
                user_id,
                f"<blockquote>You: {feedback_text}</blockquote>\n\n"
                f"<b>📩 Reply from Admin:</b>\n{admin_reply}",
                parse_mode="html"
            )
            await message.reply_text("✅ Reply sent anonymously to the user.")
        except Exception as e:
            logger.error(f"Error sending reply to user {user_id}: {e}")
            await message.reply_text("❌ Failed to send reply. The user may have blocked the bot.")
    except Exception as e:
        logger.error(f"Error in reply_to_feedback: {e}")
        
