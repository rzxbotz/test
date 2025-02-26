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
        # First, check if we're on a branch
        branch_check = subprocess.run(
            ["git", "symbolic-ref", "--short", "HEAD"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        
        # If not on a branch, checkout main
        if branch_check.returncode != 0:
            await message.reply_text("Not currently on a branch. Checking out main branch...")
            subprocess.check_call(["git", "checkout", "main"])
        
        # Now fetch changes
        await message.reply_text("Fetching latest changes...")
        subprocess.check_call(["git", "fetch", "origin", "main"])
        
        # Check if we're behind remote
        status = subprocess.check_output(
            ["git", "rev-list", "--count", "HEAD..origin/main"]
        ).decode("UTF-8").strip()
        
        if status == "0":
            return await message.reply_text("Already up-to-date!")
        
        # If we have updates, perform the merge
        await message.reply_text(f"Found {status} new updates. Updating...")
        merge_output = subprocess.check_output(
            ["git", "merge", "origin/main"]
        ).decode("UTF-8")
        
        # Install requirements
        await message.reply_text("Installing requirements...")
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        
        # Success message
        m = await message.reply_text(f"```{merge_output}```")
        await m.edit("**Updated with main branch, restarting now...**")
        
        # Restart
        restart()
    except Exception as e:
        return await message.reply_text(f"Update failed: {str(e)}")

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