from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from config import START_PIC

@Client.on_message(filters.command("about") & filters.incoming)
async def about(client, message):
    buttons = [[
        InlineKeyboardButton("Learn More About Us!", callback_data="abouts")
    ],[
        InlineKeyboardButton("Credit", callback_data="credit")
    ],[
        InlineKeyboardButton("𝖢𝗅𝗈𝗌𝖾", callback_data="close_data")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_photo(
        photo=START_PIC,  # Now using START_PIC from script.py
        caption=script.ABOUT_TXT,
        reply_markup=reply_markup
    )
