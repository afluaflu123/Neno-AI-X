import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]
BOT_START_TIME = time.time()

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - BOT_START_TIME))
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms\n➪ 𝖡𝗈𝗍 𝖴𝗉𝗍𝗂𝗆𝖾: {uptime}")
                  
