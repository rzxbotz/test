from pyrogram import Client, filters
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Script import script
from config import START_PIC

@Bot.on_message(filters.command("about"))
async def about(client, message):
    buttons = [
        [InlineKeyboardButton("Learn More About Us", callback_data="abouts")],
        [InlineKeyboardButton("Credits", callback_data="credit")],
        [InlineKeyboardButton("Close", callback_data="close")]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_photo(
        photo=START_PIC,  
        caption=script.ABOUT_TXT,
        reply_markup=reply_markup
    )

@Bot.on_callback_query(filters.regex("close_data"))
async def close_callback(client, callback_query):
    try:
        # Delete the message with the button
        await callback_query.message.delete()
        # Answer the callback query to stop the loading animation
        await callback_query.answer("Closed!")
    except Exception as e:
        print(f"Error in close callback: {e}")
        await callback_query.answer("Something went wrong!", show_alert=True)
