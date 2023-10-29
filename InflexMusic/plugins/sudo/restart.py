import asyncio
import os
import shutil
import socket
from datetime import datetime

import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters

import config
from config import OWNER_ID
from InflexMusic import app
from InflexMusic.misc import HAPP, SUDOERS, XCB
from InflexMusic.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from InflexMusic.utils.decorators.language import language
from InflexMusic.utils.pastebin import InflexBin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


@app.on_message(filters.command(["getlog", "logs", "getlogs"]) & filters.user(OWNER_ID))
@language
async def log_(client, message, _):
    try:
        await message.reply_document(document="log.txt")
    except:
        await message.reply_text(_["server_1"])


@app.on_message(filters.command(["update", "gitpull"]) & filters.user(OWNER_ID))
@language
async def update_(client, message, _):
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["server_2"])
    response = await message.reply_text(_["server_3"])
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(_["server_4"])
    except InvalidGitRepositoryError:
        return await response.edit(_["server_5"])
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]
    for checks in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit(_["server_6"])
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: <a href={REPO_}/commit/{info}>{info.summary}</a> 𝖡𝗒 -> {info.author}</b>\n\t\t\t\t<b>➥ 𝖢𝗈𝗆𝗆𝗂𝗍𝗍𝖾𝖽 𝖮𝗇 :</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>𝖠 𝖭𝖾𝗐 𝖴𝗉𝖽𝖺𝗍𝖾 𝖨𝗌 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖥𝗈𝗋 𝖳𝗁𝖾 𝖡𝗈𝗍 !</b>\n\n➣ 𝖯𝗎𝗌𝗁𝗂𝗇𝗀 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖭𝗈𝗐\n\n<b><u>𝖴𝗉𝖽𝖺𝗍𝖾𝗌 :</u></b>\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await InflexBin(updates)
        nrs = await response.edit(
            f"<b>𝖠 𝖭𝖾𝗐 𝖴𝗉𝖽𝖺𝗍𝖾 𝖨𝗌 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖥𝗈𝗋 𝖳𝗁𝖾 𝖡𝗈𝗍 !</b>\n\n➣ 𝖯𝗎𝗌𝗁𝗂𝗇𝗀 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖭𝗈𝗐\n\n<u><b>𝖴𝗉𝖽𝖺𝗍𝖾𝗌 :</b></u>\n\n<a href={url}>𝖢𝗁𝖾𝖼𝗄 𝖴𝗉𝖽𝖺𝗍𝖾𝗌</a>"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    os.system("git stash &> /dev/null && git pull")

    try:
        served_chats = await get_active_chats()
        for x in served_chats:
            try:
                await app.send_message(
                    chat_id=int(x),
                    text=_["server_8"].format(app.mention),
                )
                await remove_active_chat(x)
                await remove_active_video_chat(x)
            except:
                pass
        await response.edit(f"{nrs.text}\n\n{_['server_7']}")
    except:
        pass

    if await is_heroku():
        try:
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            await response.edit(f"{nrs.text}\n\n{_['server_9']}")
            return await app.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=_["server_10"].format(err),
            )
    else:
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && bash start")
        exit()


@app.on_message(filters.command(["restart"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀 ...")
    ac_chats = await get_active_chats()
    for x in ac_chats:
        try:
            await app.send_message(
                chat_id=int(x),
                text=f"{app.mention} 𝖨𝗌 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀 ...\n\n𝖸𝗈𝗎 𝖢𝖺𝗇 𝖲𝗍𝖺𝗋𝗍 𝖯𝗅𝖺𝗒𝗂𝗇𝗀 𝖠𝖿𝗍𝖾𝗋 15 - 20 𝖲𝖾𝖼𝗈𝗇𝖽𝗌 .",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except:
            pass

    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text(
        "» 𝖱𝖾𝗌𝗍𝖺𝗋𝗍 𝖯𝗋𝗈𝖼𝖾𝗌𝗌 𝖲𝗍𝖺𝗋𝗍𝖾𝖽 , 𝖯𝗅𝖾𝖺𝗌𝖾 𝖶𝖺𝗂𝗍 𝖥𝗈𝗋 𝖥𝖾𝗐 𝖲𝖾𝖼𝗈𝗇𝖽𝗌 𝖴𝗇𝗍𝗂𝗅 𝖳𝗁𝖾 𝖡𝗈𝗍 𝖲𝗍𝖺𝗋𝗍𝗌 ...."
    )
    os.system(f"kill -9 {os.getpid()} && python3 -m InflexMusic")
