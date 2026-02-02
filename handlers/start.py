from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.client import app
from utils.force_subscribe import is_user_subscribed
from config.env import FORCE_SUB_CHANNEL_INVITE, FORCE_SUB_CHANNEL_ID

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    user_id = message.from_user.id

    is_allowed = await is_user_subscribed(client, user_id)

    if not is_allowed:
        join_button = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔔 Join Channel", url=FORCE_SUB_CHANNEL_INVITE)],
                [InlineKeyboardButton("✅ I’ve Joined", callback_data="check_joined")]
            ]
        )

        await message.reply_text(
            "🚫 To use this bot, you must join our channel first.",
            reply_markup=join_button
        )
        return

    await message.reply_text("✅ Access granted!\nYou can now use the bot.")