import logging
from pyrogram import Client, filters, enums
from pyrogram.types import Message

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Admin Channel ID (Replace with the correct one)
ADMIN_CHANNEL_ID = -1001906863982

# Admin User ID
ADMIN_USER_ID = 6051042088  # Replace with the actual admin user ID

@Client.on_message(filters.private & ~filters.user(ADMIN_USER_ID) & filters.command("feedback"))
async def submit_feedback(client: Client, message: Message):
    """Immediately submits feedback to the admin channel."""
    try:
        user_id = message.chat.id
        user_message = message.text.split(" ", 1)

        if len(user_message) < 2:
            await message.reply_text(
                "To submit feedback, please use the correct format:\n\n"
                "Example: /feedback This bot is very useful.\n\n"
                "Your feedback helps us improve. Thank you."
            )
            return

        feedback_text = user_message[1]
        user = await client.get_users(user_id)
        user_name = user.first_name
        mention = f"<a href='tg://user?id={user_id}'>{user_name}</a>"  # HTML format

        # Send feedback to the admin channel using HTML
        await client.send_message(
            ADMIN_CHANNEL_ID,
            f"<b>New Feedback Received</b>\n\n"
            f"<b>Message:</b>\n{feedback_text}\n\n"
            f"<b>User:</b> {mention}\n"
            f"<b>User ID:</b> <code>{user_id}</code>",
            parse_mode=enums.ParseMode.HTML
        )

        await message.reply_text("Your feedback has been submitted successfully. Thank you.")
    
    except Exception as e:
        logger.error(f"Error in submit_feedback: {e}")
        await message.reply_text("An error occurred while submitting your feedback. Please try again later.")

@Client.on_message(filters.channel & filters.reply)
async def reply_to_feedback(client: Client, message: Message):
    """Admin replies are sent anonymously via the bot."""
    try:
        replied_message = message.reply_to_message

        if not replied_message or not replied_message.text:
            return

        # Initialize variables
        user_id = None
        feedback_text = None

        lines = replied_message.text.split("\n")

        # Extract User ID and Feedback Message
        for i, line in enumerate(lines):
            if "User ID:" in line:
                try:
                    user_id = int(line.split("<code>")[1].split("</code>")[0])
                except (IndexError, ValueError):
                    logger.error("Failed to extract User ID from feedback message.")
                    await message.reply_text("Error: Could not extract User ID.")
                    return
            elif "Message:" in line:
                feedback_text = "\n".join(lines[i+1:]).strip()

        if not user_id:
            await message.reply_text("Error: Could not extract User ID.")
            return

        admin_reply = message.text

        try:
            await client.send_message(
                user_id,
                f"<b>Your Feedback:</b> {feedback_text or 'No message found'}\n\n"
                f"<b>Reply from Admin:</b>\n{admin_reply}",
                parse_mode=enums.ParseMode.HTML
            )
            await message.reply_text("Reply sent anonymously to the user.")
        except Exception as e:
            logger.error(f"Error sending reply to user {user_id}: {e}")
            await message.reply_text("Failed to send reply. The user may have blocked the bot.")
    except Exception as e:
        logger.error(f"Error in reply_to_feedback: {e}")
        
