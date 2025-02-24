# (©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Script import script

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "course":
        await query.message.edit_text(
            text=script.COURSE.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BCOM", callback_data="bcom"),
                        InlineKeyboardButton("BCOM", callback_data="soon")
                    ],[
                        InlineKeyboardButton("Back", callback_data="start")
                    ]
                ]
            )
        )

    elif data == "bcom":  # Fixed case issue
        await query.message.edit_text(
            text=script.BCOM.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Admission Onwards 2019", callback_data="bcm2019"),
                        InlineKeyboardButton("Admission Onwards 2024", callback_data="soon")
                    ],[
                        InlineKeyboardButton("Back", callback_data="course")
                    ]
                ]
            )
        )

    elif data == "bcm2019":  # Fixed case issue
        await query.message.edit_text(
            text=script.MATERIALS2019.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Study Notes", callback_data="studynotes2019"),
                    ],[
                        InlineKeyboardButton("Question Papers", callback_data="pyq2019")
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data="bcom")
                    ]
                ]
            )
        )

    elif data == "studynotes2019":  # Fixed case issue
        await query.message.edit_text(
            text=script.BCM2019SNSEMESTERS.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
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
                    [
                        InlineKeyboardButton("Back", callback_data="bcm2019")
                    ]
                ]
            )
        )

    elif data == "bcmsnsem1":  
        await query.message.edit_text(
            text=script.BCMSNSEM1.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="studynotes2019")
                    ]
                ]
            )
        )

    elif data == "bcmsnsem2":  
        await query.message.edit_text(
            text=script.BCMSNSEM2.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="studynotes2019")
                    ]
                ]
            )
        )

    elif data == "bcmsnsem3":  
        await query.message.edit_text(
            text=script.BCMSNSEM3.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="studynotes2019")
                    ]
                ]
            )
        )

    elif data == "bcmsnsem4": 
        await query.message.edit_text(
            text=script.BCMSNSEM4.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="studynotes2019")
                    ]
                ]
            )
        )

    elif data == "bcmsnsem5":  
        await query.message.edit_text(
            text=script.BCMSNSEM5.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="studynotes2019")
                    ]
                ]
            )
        )

    elif data == "bcmsnsem6":
        await query.message.edit_text(
            text=script.BCMSNSEM6.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="studynotes2019")
                    ]
                ]
            )
        )

    elif data == "pyq2019":  # Fixed case issue
        await query.message.edit_text(
            text=script.BCM2019PYQSEMESTERS.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
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
                    [
                        InlineKeyboardButton("Back", callback_data="bcm2019")
                    ]
                ]
            )
        )

    elif data == "bcmpyqsem1":  
        await query.message.edit_text(
            text=script.BCMPYQSEM1.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="pyq2019")
                    ]
                ]
            )
        )

    elif data == "bcmpyqsem2":  
        await query.message.edit_text(
            text=script.BCMPYQSEM2.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="pyq2019")
                    ]
                ]
            )
        )

    elif data == "bcmpyqsem3":  
        await query.message.edit_text(
            text=script.BCMPYQSEM3.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="pyq2019")
                    ]
                ]
            )
        )

    elif data == "bcmpyqsem4": 
        await query.message.edit_text(
            text=script.BCMPYQSEM4.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="pyq2019")
                    ]
                ]
            )
        )

    elif data == "bcmpyqsem5":  
        await query.message.edit_text(
            text=script.BCMPYQSEM5.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="pyq2019")
                    ]
                ]
            )
        )

    elif data == "bcmpyqsem6":
        await query.message.edit_text(
            text=script.BCMPYQSEM6.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Back", callback_data="pyq2019")
                    ]
                ]
            )
        )

    elif data == "soon":
    await query.answer(
        text="This feature will be available soon!",  # Alert message text
        show_alert=True  # Setting this to True shows a pop-up alert
    )
    
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
