from pyrogram.enums import ParseMode

from InflexMusic import app
from InflexMusic.utils.database import is_on_off
from config import LOG_GROUP_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} 𝖯𝗅𝖺𝗒 𝖫𝗈𝗀</b>

<b>𝖢𝗁𝖺𝗍 𝖨𝖣 :</b> <code>{message.chat.id}</code>
<b>𝖢𝗁𝖺𝗍 𝖭𝖺𝗆𝖾 :</b> {message.chat.title}
<b>𝖢𝗁𝖺𝗍 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :</b> @{message.chat.username}

<b>𝖴𝗌𝖾𝗋 𝖨𝖣 :</b> <code>{message.from_user.id}</code>
<b>𝖭𝖺𝗆𝖾 :</b> {message.from_user.mention}
<b>𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :</b> @{message.from_user.username}

<b>𝖰𝗎𝖾𝗋𝗒 :</b> {message.text.split(None, 1)[1]}
<b>𝖲𝗍𝗋𝖾𝖺𝗆-𝖳𝗒𝗉𝖾 :</b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
