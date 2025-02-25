from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(
                text="📩 Forward the **First Message** from DB Channel (with Quotes) or Send the DB Channel Post Link.",
                chat_id=message.from_user.id, 
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)), 
                timeout=60
            )
        except:
            return await message.reply("⏳ Timeout! Please try again.")

        f_msg_id = await get_message_id(client, first_message)

        if f_msg_id and first_message.forward_from_chat and first_message.forward_from_chat.id == client.db_channel.id:
            break
        else:
            await first_message.reply("❌ **Error**\n\nThis is not a valid message from the DB Channel!", quote=True)

    while True:
        try:
            second_message = await client.ask(
                text="📩 Forward the **Last Message** from DB Channel (with Quotes) or Send the DB Channel Post Link.",
                chat_id=message.from_user.id, 
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)), 
                timeout=60
            )
        except:
            return await message.reply("⏳ Timeout! Please try again.")

        s_msg_id = await get_message_id(client, second_message)

        if s_msg_id and second_message.forward_from_chat and second_message.forward_from_chat.id == client.db_channel.id:
            break
        else:
            await second_message.reply("❌ **Error**\n\nThis is not a valid message from the DB Channel!", quote=True)

    encoded_string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(encoded_string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔗 Share Link", url=f'https://telegram.me/share/url?url={link}')]]
    )
    
    await second_message.reply_text(
        f"✅ **Batch Link Generated!**\n\n🔗 **Here is your link:**\n`{link}`", 
        quote=True, 
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(
                text="📩 Forward a **Message** from the DB Channel (with Quotes) or Send the DB Channel Post Link.",
                chat_id=message.from_user.id, 
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)), 
                timeout=60
            )
        except:
            return await message.reply("⏳ Timeout! Please try again.")

        msg_id = await get_message_id(client, channel_message)

        if msg_id and channel_message.forward_from_chat and channel_message.forward_from_chat.id == client.db_channel.id:
            break
        else:
            await channel_message.reply("❌ **Error**\n\nThis is not a valid message from the DB Channel!", quote=True)

    encoded_string = f"get-{msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(encoded_string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔗 Share Link", url=f'https://telegram.me/share/url?url={link}')]]
    )
    
    await channel_message.reply_text(
        f"✅ **Single Message Link Generated!**\n\n🔗 **Here is your link:**\n`{link}`", 
        quote=True, 
        reply_markup=reply_markup
    )
