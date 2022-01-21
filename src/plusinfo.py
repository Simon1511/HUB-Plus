# plusinfo
# HUB++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from os.path import basename

ehandler = EventHandler()
VERSION = "2022.1.2"

@ehandler.on(command="plusver", hasArgs=True, outgoing=True)
async def plus(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        await event.edit(f"You're running HUB++ version {VERSION}.\n__Note: this is the version of plusinfo, other modules might have different versions. We recommend users to update every module they have installed.__")

_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')