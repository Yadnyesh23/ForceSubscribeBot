from pyrogram import filters
from pyrogram.types import CallbackQuery
from app.client import app
from utils.force_subscribe import is_user_subscribed
from config.env import FORCE_SUB_CHANNEL_ID

@app.on_callback_query(filters.regex("check_joined"))
async def check_joined_callback( app, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    is_allowed = await is_user_subscribed(app, user_id)

    if is_allowed:
        await callback_query.answer("✅ Membership confirmed!", show_alert=True)
        await callback_query.message.edit_text("✅ Access granted!\nYou can now use the bot.")
    else:
        await callback_query.answer("❌ You still haven't joined the channel.", show_alert=True)