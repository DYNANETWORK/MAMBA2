from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from telethon.errors.rpcerrorlist import YouBlockedUserError

from PYTHONBOT.utils import admin_cmd, sudo_cmd
from userbot import CMD_LIST, bot
from userbot.Config import Config

from . import *

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

msg = f"""
**β π»ππππππππ’ π°π Pythonπ±ππ β**
  β’        [β₯οΈ ππππ β₯οΈ](https://github.com/LEGEND-LX/PYTHONBOT-V9)
  β’        [β¦οΈ REPL β¦οΈ](https://replit.com/@LEGEND-LX/PYTHONBOT-4#main.py)
  β’  Β©οΈ {Python_channel} β’
"""


@bot.on(admin_cmd(pattern="repo$"))
@bot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def repo(event):
    try:
        python = await bot.inline_query(botname, "repo")
        await python[0].click(event.chat_id)
        if event.sender_id == Legendl_Mr_Hacker:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@bot.on(admin_cmd(pattern="legend ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="legend ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = botname
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "pythonbot_help")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            python = await eor(
                event,
                "**Inline Mode is disabled.** \n__Turning it on, please wait for a minute...__",
            )
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await python.edit("Unblock @Botfather first.")
                await python.edit(
                    f"**Turned On Inline Mode Successfully.** \n\nDo `{l1}legend` again to get the help menu."
                )
            await bot.delete_messages(
                conv.chat_id,
                [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
            )
    else:
        await eor(
            event,
            "**β οΈ π΄πππΎπ !!** \nπΏπππππ ππ-π²ππππ BOT_TOKEN & BOT_USERNAME on Heroku.",
        )


@bot.on(admin_cmd(pattern="op ?(.*)", outgoing=True))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = botname
    input_str = event.pattern_match.group(1)
    if tgbotusername is not None or PYTHON_input == "text":
        results = await event.client.inline_query(tgbotusername, "pythonbot_help")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await eor(event, "**Check Bot Token And Bot Username In Reveal Var*")

        if input_str in CMD_LIST:
            string = "Commands found in {}:\n".format(input_str)
            for i in CMD_LIST[input_str]:
                string += "  " + i
                string += "\n"
            await event.edit(string)
        else:
            await event.edit(input_str + " is not a valid plugin!")


@bot.on(admin_cmd(pattern="plinfo(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="plinfo(?: |$)(.*)", allow_sudo=True))
async def pythonbott(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eor(event, "**β οΈ π΄ππππ !** \nπ½πππ π Plugin ππππ ππ ππππ  ππππππ ππππ")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`β¦οΈ`"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eor(
            event,
            "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string,
        )


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602

    result = result.stringify()

    logger.info(result)  # pylint:disable=E0602

    await event.edit("ΡΡβΡΡΠ½ΟΞ·  Π²Ξ±ΡΡβ ΟΡΡΡΠ²ΟΡ ΟΟΟΡΡΡβ Π²Ρ **PythonαΊΓΈβ ** Π²ΟΡ")
