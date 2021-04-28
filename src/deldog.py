# deldog
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import asyncio
from datetime import datetime
import os
import requests

from userbot import tgclient
from userbot.include.aux_funcs import module_info
from telethon.events import NewMessage
from os.path import basename
from os.path import join as pathjoin
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.config import TEMP_DL_DIR

ehandler = EventHandler()
VERSION = "2021.4 for HUB 4.x"

def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))

@ehandler.on(command="dog", hasArgs=True, outgoing=True)
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = "Syntax: `.dog <text>`"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            await event.edit("`Downloading file...`")
            downloaded_file_name = await bot.download_media(
                previous_message,
                TEMP_DL_DIR,
                progress_callback=progress
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        await event.edit("Syntax: `.dog <text>`")
    if message == "Syntax: `.dog <text>`":
        await event.edit("Syntax: `.dog <text>`")
        return
    await event.edit("`Uploading...`")
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    end = datetime.now()
    ms = (end - start).seconds
    if r["isUrl"]:
        nurl = f"https://del.dog/v/{r['key']}"
        await event.edit("Pasted to {} in {} seconds. [link]({}).".format(url, ms, nurl))
    else:
        await event.edit("Pasted to {} in {} seconds.".format(url, ms))
        
register_module_desc("Upload text to Del.dog.")
register_cmd_usage("dog", "<optional text>", "Upload text to Del.dog. If no text argument is provided uploads the message replied to.")
register_module_info(
    name="Del.dog",
    authors="githubcatw, help from prototype74",
    version=VERSION
)