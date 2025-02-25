from bot import Bot
import os, sys, asyncio, re, time, shutil, psutil, subprocess
from pyrogram.types import Message
from pyrogram import filters, enums
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

# Set bot uptime at startup
Bot.uptime = datetime.now()

### BOT STATS COMMAND ###
@Bot.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    """Show bot uptime"""
    now = datetime.now()
    delta = now - bot.uptime
    uptime = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=uptime))

### AUTO REPLY TO PRIVATE MESSAGES ###
@Bot.on_message(filters.private & filters.incoming)
async def auto_reply(_, message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)

### RESTART FUNCTION ###
async def restart():
    """Restart the bot by exiting the process (Koyeb will restart automatically)"""
    os._exit(0)  # Forces exit, Koyeb auto-restarts

### UPDATE & RESTART COMMAND ###
@Bot.on_message(filters.command("update") & filters.user(ADMINS))
async def update_restart(app, message):
    """Pull updates from GitHub and restart the bot"""
    try:
        subprocess.run(["git", "reset", "--hard"], check=True)  # Reset local changes
        update_output = subprocess.run(["git", "pull"], capture_output=True, text=True).stdout

        if "Already up to date." in update_output:
            return await message.reply_text("✅ Bot is already up-to-date!")

        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

        await message.reply_text(f"**🆕 Updated Successfully!**\n```{update_output}```")
        await restart()  # Restart the bot after update
    except subprocess.CalledProcessError as e:
        await message.reply_text(f"❌ Update failed!\n```{e.stderr}```")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

### RESTART COMMAND ###
@Bot.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_command(app, message):
    """Handle the restart command"""
    await message.reply_text("♻️ Restarting bot...")
    await restart()

### SERVER STATUS COMMAND ###
@Bot.on_message(filters.command("server") & filters.user(ADMINS))
async def server_stats(b, m):
    """Show server stats"""
    total, used, free = shutil.disk_usage("/")  # Use "/" for correct disk usage
    ram = psutil.virtual_memory()
    cpu = psutil.cpu_percent()

    start_t = time.time()
    sts = await m.reply_text("⏳ Gathering server stats...")
    end_t = time.time()
    ping = (end_t - start_t) * 1000

    stats = f"""
<b>📡 Server Stats:</b>
─────────────────────
⏳ <b>Ping:</b> {ping:.2f} ms
💽 <b>Total Disk:</b> {get_size(total)}
📂 <b>Used Disk:</b> {get_size(used)}
📁 <b>Free Disk:</b> {get_size(free)}
🖥️ <b>Total RAM:</b> {get_size(ram.total)}
🎛 <b>Used RAM:</b> {get_size(ram.used)}
🧠 <b>Free RAM:</b> {get_size(ram.available)}
⚙️ <b>CPU Usage:</b> {cpu}%
📊 <b>Disk Usage:</b> {psutil.disk_usage('/').percent}%
    """
    await sts.edit(stats, parse_mode=enums.ParseMode.HTML)

### SIZE CONVERSION FUNCTION ###
def get_size(size_in_bytes):
    """Convert bytes to a human-readable format"""
    if size_in_bytes == 0:
        return "0B"
    size_units = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    while size_in_bytes >= 1024 and i < len(size_units) - 1:
        size_in_bytes /= 1024
        i += 1
    return f"{size_in_bytes:.2f} {size_units[i]}"
    
