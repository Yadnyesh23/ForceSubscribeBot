from app.client import app
from pyrogram import Client, filters

@app.on_message(filters.command('start'))
async def start_handler(client , message):
    await message.reply_text("Bot is running ✅\nStep 1 completed.")