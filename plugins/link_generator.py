#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id
import re

# Pattern to detect command-like text (starts with / followed by letters)
COMMAND_PATTERN = re.compile(r'^\/[a-zA-Z]+')

async def is_command_like(text):
    """Check if the given text looks like a command."""
    if not text:
        return False
    # Check if the text starts with a slash followed by letters
    return bool(COMMAND_PATTERN.match(text.strip()))

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            # Check if the message content looks like a command
            if first_message.text and await is_command_like(first_message.text):
                await first_message.reply("❌ Error\n\nI cannot process command-like texts (starting with /). Please forward a different message.", quote=True)
                continue
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote=True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            # Check if the message content looks like a command
            if second_message.text and await is_command_like(second_message.text):
                await second_message.reply("❌ Error\n\nI cannot process command-like texts (starting with /). Please forward a different message.", quote=True)
                continue
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote=True)
            continue

    # Also verify the actual content of the messages in the DB channel
    try:
        first_content = await client.get_messages(client.db_channel.id, f_msg_id)
        second_content = await client.get_messages(client.db_channel.id, s_msg_id)
        
        # Check if either message contains command-like text
        if (first_content.text and await is_command_like(first_content.text)) or \
           (second_content.text and await is_command_like(second_content.text)):
            await second_message.reply("❌ Error\n\nOne of the selected messages contains command-like text (starting with /). I cannot generate links for commands.", quote=True)
            return
    except Exception as e:
        await second_message.reply(f"❌ Error\n\nFailed to verify message content: {str(e)}", quote=True)
        return

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            # Check if the message content looks like a command
            if channel_message.text and await is_command_like(channel_message.text):
                await channel_message.reply("❌ Error\n\nI cannot process command-like texts (starting with /). Please forward a different message.", quote=True)
                continue
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote=True)
            continue

    # Verify the actual content of the message in the DB channel
    try:
        content = await client.get_messages(client.db_channel.id, msg_id)
        if content.text and await is_command_like(content.text):
            await channel_message.reply("❌ Error\n\nThe selected message contains command-like text (starting with /). I cannot generate links for commands.", quote=True)
            return
    except Exception as e:
        await channel_message.reply(f"❌ Error\n\nFailed to verify message content: {str(e)}", quote=True)
        return

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)