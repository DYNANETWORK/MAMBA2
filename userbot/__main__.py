from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, MAMBAversion
from pathlib import Path
import asyncio
import glob
import telethon.utils
l2= Config.SUDO_COMMAND_HAND_LER
MAMBA_PIC = Config.ALIVE_PIC or "https://te.legra.ph/file/a8a793a8716bdcc923fd3.jpg"
l1 = Config.COMMAND_HAND_LER


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"MAMBA_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        print("Startup Completed")
    else:
        bot.start()
print("Loading Modules / Plugins")


async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))
"""
async def assistant():
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

        extra_repo = "https://github.com/SUKHPAL443/MAMBA2"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("Loading Addons")
        path = "MAMBA2/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[MAMBABOT-PRO] - Addons -  Installed - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[MAMBABOT-PRO] - Addons - ERROR - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
"""

print(f"""『🔱MAMBA USERBOT🔱』➙𖤍࿐ IS ON!!! MAMBA VERSION :- {MAMBAversion}
TYPE :- " .gpromote @BLACKMAMBA_OFFICIAL " OR .python OR .ping CHECK IF I'M ON!
╔════❰MAMBA USERBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - BLACKMAMBA
║┣⪼{MAMBA_PIC}
║┣⪼ CREATOR -@BLACKMAMBA_OFFICIAL
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱MAMBA USERBOT 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")



async def mamba_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                MMABA_PIC,
                caption=f"#START \n\nDeployed MAMBA USERBOT Successfully\n\n**MAMBABOT- {MAMBAversion}**\n\nType `{l1}legend` or `{l1}alive` to check! \n\nJoin [MAMBABOT Channel](t.me/MAMBA_NETWORK) for Updates & [MAMBA Chat](t.me/MAMBA_X_SUPPORT) for any query regarding MAMBA BOT",
            )
    except Exception as e:
        print(str(e))

# Join MAMBA Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@MAMBA_NETWORK"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@MAMBA_X_SUPPORT"))
    except BaseException:
         pass


bot.loop.create_task(python_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
