from pyrogram import Client, filters
import asyncio

# Settings
DELETE_DELAY = 3  # Delay before deleting the message (set to 0 for instant delete)
SEND_WARNING = True  # Set to True if you want to warn users before deletion

@Client.on_message(filters.private & filters.forwarded)
async def delete_forwarded(client, message):
    try:
        user_id = message.chat.id
        message_id = message.id  # FIXED: Correct attribute name

        if SEND_WARNING:
            warning_msg = await message.reply_text(
                "🚫 Forwarded messages are not allowed. Your message will be deleted.",
                quote=True
            )
            await asyncio.sleep(DELETE_DELAY)  # Wait before deleting

        await message.delete()  # Delete the forwarded message

        if SEND_WARNING:
            await warning_msg.delete()  # Delete the warning message

        print(f"Deleted forwarded message from user {user_id}")

    except Exception as e:
        print(f"Error deleting message: {e}")
        
