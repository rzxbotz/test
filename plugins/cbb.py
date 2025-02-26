# (©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_PIC
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from Script import script

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    async def safe_edit_media(new_caption, reply_markup):
        """Check if the new caption is different before editing media"""
        if query.message.caption != new_caption:
            try:
                await query.message.edit_media(
                    InputMediaPhoto(START_PIC, caption=new_caption),
                    reply_markup=reply_markup
                )
            except Exception as e:
                print(f"Error editing media: {e}")

    if data == "start":
        await safe_edit_media(
            script.COURSE.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("SELECT YOUR COURSE", callback_data="course")
                    ],
                    [
                        InlineKeyboardButton("UPDATES", url="https://t.me/ExamWallet"),
                        InlineKeyboardButton("SUPPORT", url="https://t.me/Exam_Wallet")
                    ]
                ]
            )
        )

    elif data == "course":
        await safe_edit_media(
            script.BCOM.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BCOM", callback_data="bcom"),
                        InlineKeyboardButton("BBA", callback_data="soon")
                    ],
                    [InlineKeyboardButton("Back", callback_data="start")]
                ]
            )
        )

    elif data == "about":
        await safe_edit_media(
            script.ABOUT_TXT.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Learn More About Us!", callback_data="abouts")
                    ],[
                        InlineKeyboardButton("Credit", callback_data="credit")
                    ],
                    [InlineKeyboardButton("Close", callback_data="close_data")]
                ]
            )
        )

    elif data == "abouts":
        await safe_edit_media(
            script.ABOUT.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="about")]
                ]
            )
        )

    elif data == "credit":
        await safe_edit_media(
            script.CREDIT.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="about")]
                ]
            )
        )

    elif data == "bcom":
        await safe_edit_media(
            script.BCOM.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Admission Onwards 2019", callback_data="bcm2019")
                    ],
                    [
                        InlineKeyboardButton("Admission Onwards 2024", callback_data="soon")
                    ],
                    [InlineKeyboardButton("Back", callback_data="course")]
                ]
            )
        )

    elif data == "bcm2019":
        await safe_edit_media(
            script.MATERIALS2019.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Study Notes", callback_data="studynotes2019")],
                    [InlineKeyboardButton("Question Papers", callback_data="pyq2019")],
                    [InlineKeyboardButton("Back", callback_data="bcom")]
                ]
            )
        )

    elif data == "studynotes2019":
        await safe_edit_media(
            script.BCM2019SNSEMESTERS.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("1️⃣ SEMESTER", callback_data="bcmsnsem1"),
                        InlineKeyboardButton("2️⃣ SEMESTER", callback_data="bcmsnsem2")
                    ],
                    [
                        InlineKeyboardButton("3️⃣ SEMESTER", callback_data="bcmsnsem3"),
                        InlineKeyboardButton("4️⃣ SEMESTER", callback_data="bcmsnsem4")
                    ],
                    [
                        InlineKeyboardButton("5️⃣ SEMESTER", callback_data="bcmsnsem5"),
                        InlineKeyboardButton("6️⃣ SEMESTER", callback_data="bcmsnsem6")
                    ],
                    [InlineKeyboardButton("Back", callback_data="bcm2019")]
                ]
            )
        )

    elif data.startswith("bcmsnsem"):
        semester = data[-1]  # Extract semester number
        await safe_edit_media(
            getattr(script, f"BCMSNSEM{semester}").format(query.from_user.mention),
            InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="studynotes2019")]]
            )
        )

    elif data == "pyq2019":
        await safe_edit_media(
            script.BCM2019PYQSEMESTERS.format(query.from_user.mention),
            InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("1️⃣ SEMESTER", callback_data="bcmpyqsem1"),
                        InlineKeyboardButton("2️⃣ SEMESTER", callback_data="bcmpyqsem2")
                    ],
                    [
                        InlineKeyboardButton("3️⃣ SEMESTER", callback_data="bcmpyqsem3"),
                        InlineKeyboardButton("4️⃣ SEMESTER", callback_data="bcmpyqsem4")
                    ],
                    [
                        InlineKeyboardButton("5️⃣ SEMESTER", callback_data="bcmpyqsem5"),
                        InlineKeyboardButton("6️⃣ SEMESTER", callback_data="bcmpyqsem6")
                    ],
                    [InlineKeyboardButton("Back", callback_data="bcm2019")]
                ]
            )
        )

    elif data.startswith("bcmpyqsem"):
        semester = data[-1]  # Extract semester number
        await safe_edit_media(
            getattr(script, f"BCMPYQSEM{semester}").format(query.from_user.mention),
            InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="pyq2019")]]
            )
        )

    elif data == "soon":
        await query.answer(
            text="This feature will be available soon!",
            show_alert=True
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
        
