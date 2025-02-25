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

        # Send feedback to the admin channel
        await client.send_message(
            ADMIN_CHANNEL_ID,
            f"<b>📩 New Feedback Received \n\n💬 Message:\n{feedback_text}\n\n👤 User: {mention}\n🆔 User ID: `{user_id}`</b>"
        )

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
        for line in replied_message.text.split("\n"):
            if "🆔 **User ID:**" in line:
                user_id = int(line.split("`")[1])
                break

        if not user_id:
            return  

        admin_reply = message.text

        try:
            await client.send_message(
                user_id,
                f"</blockquote>You : {feedback_text}</blockquote>\n\n<b>Reply from admin : {admin_reply}</b>"
            )
            await message.reply_text("✅ Reply sent anonymously to the user.")
        except Exception as e:
            logger.error(f"Error sending reply to user {user_id}: {e}")
            await message.reply_text("❌ Failed to send reply. The user may have blocked the bot.")
    except Exception as e:
        logger.error(f"Error in reply_to_feedback: {e}")
        
