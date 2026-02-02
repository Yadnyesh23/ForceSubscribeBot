from pyrogram import Client
from config.env import BOT_TOKEN

app = Client(
    "force_subscribe_bot",
    bot_token=BOT_TOKEN
)