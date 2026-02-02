from pyrogram.errors import UserNotParticipant
from config.env import FORCE_SUB_CHANNEL_ID

async def is_user_subscribed(client, user_id: int) -> bool:
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB_CHANNEL_ID, user_id=user_id)
        return member.status in ("member", "administrator", "creator", "owner")
    except UserNotParticipant:
        return False
    except Exception as e:
        print(f"Force subscribe check error: {e}")
        return False