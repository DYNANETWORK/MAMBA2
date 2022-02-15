from telethon import events
from . import *
from userbot import ALIVE_NAME
from userbot import bot

PYTHON_USER = bot.me.first_name
Legendl_Mr_Hacker = bot.uid
python_mention = f"[{PYTHON_USER}](tg://user?id={Legendl_Mr_Hacker})"

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PYTHON"


PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『I N PYTHONBOT』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{python_mention}』\n"
pm_caption += f"**╭──────────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『Pythonẞø†』~ `{PYTHONversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Python_Updata)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/LEGEND-LX/PYTHONBOT-V9.0.8/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『Pythonẞø†』 ](https://t.me/Python_Userbot_Support)\n"
pm_caption += f"┣Assistant ~ By [『Legend-Lx』 ](https://t.me/Legendl_Mr_Hacker)\n"
pm_caption += f"╰──────────────\n"
pm_caption += f"       »»» [『Pythonẞø†』](https://t.me/Python_Userbot_Support) «««"


# only Owner Can Use it

@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
