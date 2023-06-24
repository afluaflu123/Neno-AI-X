import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]
BOT_START_TIME = time.time()

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("■■■▤□□")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%HH %MM %SS", time.gmtime(time.time() - BOT_START_TIME))
    await rm.edit(f"<b>✪ ʟɪᴠᴇ ᴘɪɴɢ sᴛᴀᴛᴜs ✪\n\n🏓 ᴘɪɴɢ : {time_taken_s:.3f} ms\n\n⏰ ᴜᴘᴛɪᴍᴇ : {uptime}\n\n Nᴀɴᴄʏ ~ ☘ ²·⁰</b>")
                  
