from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN=os.getenv("BOT_TOKEN")

FORCE_SUB_CHANNEL_USERNAME = os.getenv("FORCE_SUB_CHANNEL_USERNAME") 
FORCE_SUB_CHANNEL_INVITE = os.getenv("FORCE_SUB_CHANNEL_INVITE")
FORCE_SUB_CHANNEL_ID = int(os.getenv("FORCE_SUB_CHANNEL_ID")) 



if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")

if not FORCE_SUB_CHANNEL_USERNAME:
    raise RuntimeError("FORCE_SUB_CHANNEL_USERNAME is missing")