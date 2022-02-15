# PYTHONBOT Assistant
from . import *
from telethon import Button, custom

from userbot import bot

from userbot import ALIVE_NAME
OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


PYTHON_USER = bot.me.first_name
Legendl_Mr_Hacker = bot.uid

python_mention = f"[{PYTHON_USER}](tg://user?id={Legendl_Mr_Hacker})"
PYTHON_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
PYTHON_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
PYTHON_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
PYTHON_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
PYTHON_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
PYTHONversion = "𝚅9.𝙾.8"

perf = "[ I N PYTHONBOT ]"


DEVLIST = [
    "2033517108"
]

async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
