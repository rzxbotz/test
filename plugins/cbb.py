#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "course":
        await query.message.edit_text(
            text=script.COURSE.format(query.from_user.mention),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BCOM", callback_data = "bcom"),
                        InlineKeyboardButton("BBA", callback_data = "bba")
                    ],[
                        InlineKeyboardButton("Back", callback_data = "start")
                    ]
                ]
            )
        )

    if data == "BCOM":
        await query.message.edit_text(
            text=script.SEMESTER.format(query.from_user.mention),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("1️⃣ SEMESTER", callback_data = "sem1"),
                        InlineKeyboardButton("2️⃣ SEMESTER", callback_data = "sem2")
                    ],[
                        InlineKeyboardButton("3️⃣ SEMESTER", callback_data = "sem3"),
                        InlineKeyboardButton("4️⃣ SEMESTER", callback_data = "sem4")
                    ],[
                        InlineKeyboardButton("5️⃣ SEMESTER", callback_data = "sem5"),
                        InlineKeyboardButton("6️⃣ SEMESTER", callback_data = "sem6")
                    ],[
                        InlineKeyboardButton("Back", callback_data = "course")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
