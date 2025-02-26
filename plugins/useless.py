from bot import Bot
import os, sys, asyncio, re, time, shutil, psutil
import subprocess
from pyrogram.types import Message
from pyrogram import filters, enums
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT, SERVER
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))

@Bot.on_message(filters.command("update") & filters.user(ADMINS))
async def update_restart(bot, message):
    try:
        out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
        if "Already up to date." in str(out):
            return await message.reply_text("Its already up-to date!")

        subprocess.check_output(["pip", "install", "-r", "requirements.txt"])

        m = await message.reply_text(f"```{out}```")
        await m.edit("**Updated with default branch, restarting now...**")
        # Don't await restart() - it doesn't return
        restart()
    except Exception as e:
        return await message.reply_text(str(e))

@Bot.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_command(bot, message):
    """Handle the restart command"""
    try:
        await message.reply_text("Restarting the bot...")
        # Don't await restart() - it doesn't return
        restart()
    except Exception as e:
        await message.reply_text(f"Error during restart: {e}")

@Bot.on_message(filters.command("server") & filters.user(ADMINS))
async def server_stats(bot, message):
    total, used, free = shutil.disk_usage(".")
    ram = psutil.virtual_memory()
    start_t = time.time()
    sts = await message.reply_text("ᴩʟᴇᴀꜱᴇ ᴡᴀɪᴛ...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    stats = SERVER.format(
        ping = f"{time_taken_s:.3f} ᴍꜱ",
        total = get_size(total),
        used = get_size(used),
        free = get_size(free),
        t_ram = get_size(ram.total),
        u_ram = get_size(ram.used),
        f_ram = get_size(ram.available),
        cpu_usage = psutil.cpu_percent(),
        ram_usage = psutil.virtual_memory().percent,
        disk_usage = psutil.disk_usage('/').percent,
    )
    await sts.edit(stats, parse_mode=enums.ParseMode.HTML)

def get_size(size_in_bytes):
    """Convert bytes to KB, MB, GB, etc."""
    if size_in_bytes == 0:
        return "0B"
    size_units = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    while size_in_bytes >= 1024 and i < len(size_units) - 1:
        size_in_bytes /= 1024
        i += 1
    return f"{size_in_bytes:.2f} {size_units[i]}"

def restart():
    """Restart the bot process"""
    # This function doesn't return - it replaces the current process
    os.execl(sys.executable, sys.executable, "-m", "bot")

@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)