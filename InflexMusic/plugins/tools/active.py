from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from InflexMusic import app
from config import OWNER_ID
from InflexMusic.misc import SUDOERS
from InflexMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "activevoice", "voice", "ac"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» 𝖦𝖾𝗍𝗍𝗂𝗇𝗀 𝖠𝖼𝗍𝗂𝗏𝖾-𝖵𝗈𝗂𝖼𝖾 𝖢𝗁𝖺𝗍𝗌 𝖫𝗂𝗌𝗍 ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» 𝖭𝗈 𝖠𝖼𝗍𝗂𝗏𝖾-𝖵𝗈𝗂𝖼𝖾 𝖢𝗁𝖺𝗍𝗌 𝖮𝗇 {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» 𝖫𝗂𝗌𝗍 𝖮𝖿 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖠𝖼𝗍𝗂𝗏𝖾-𝖵𝗈𝗂𝖼𝖾 𝖢𝗁𝖺𝗍𝗌 :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "activevideo", "video"]) & filters.user(OWNER_ID))
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» 𝖦𝖾𝗍𝗍𝗂𝗇𝗀 𝖠𝖼𝗍𝗂𝗏𝖾-𝖵𝗂𝖽𝖾𝗈 𝖢𝗁𝖺𝗍𝗌 𝖫𝗂𝗌𝗍 ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» 𝖭𝗈 𝖠𝖼𝗍𝗂𝗏𝖾-𝖵𝗂𝖽𝖾𝗈 𝖢𝗁𝖺𝗍𝗌 𝖮𝗇 {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» 𝖫𝗂𝗌𝗍 𝖮𝖿 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖠𝖼𝗍𝗂𝗏𝖾-𝖵𝗂𝖽𝖾𝗈 𝖢𝗁𝖺𝗍𝗌 :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
