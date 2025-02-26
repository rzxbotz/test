from pyrogram import Client, filters
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from config import START_PIC

@Bot.on_message(filters.command("about"))
async def about(client, message):
    buttons = [
        [InlineKeyboardButton("Learn More About Us", callback_data="abouts")],
        [InlineKeyboardButton("Credits", callback_data="credit")],
        [InlineKeyboardButton("Close", callback_data="close_data")]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_photo(
        photo=START_PIC,  
        caption=script.ABOUT_TXT,
        reply_markup=reply_markup
    )
