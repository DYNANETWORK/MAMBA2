
import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot.Config import Config
from telethon import version
from userbot import ALIVE_NAME, StartTime, MAMBAversion
from MAMBA.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from . import *
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "𝓜𝓐𝓜𝓑𝓐 🇮🇳"
MAMBA_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂ Choice 𝓜𝓐𝓜𝓑𝓐"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@MAMBA_X_SUPPORT"

Mamba = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={Mamba})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="malive$"))
@bot.on(sudo_cmd(pattern="malive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  MAMBA_IMG:
        MAMBA_caption = f"{CUSTOM_ALIVE_TEXT}**\n"
        
        MAMBA_caption += f"╔════❰𓆩༒𝓐𝓛𝓘𝓥𝓔 𝓛𝓘𝓝𝓤𝓧𓆩༒❱═❍⊱❁ \n"
        MAMBA_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        MAMBA_caption += f"║┣⪼𓆩༒𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻༒𓆪⭆[𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"
        MAMBA_caption += f"║┣⪼𓆩༒𝓔-𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻༒𓆪⭆[𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"
        MAMBA_caption += f"║╰━━━━━━━━━━━━━━━➣\n"
        MAMBA_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        MAMBA_caption += f"║┣⪼𓆩༒𝓜𝓔𝓝𝓣𝓘𝓞𝓝𝓑𝓞𝓣༒𓆪⭆[𝐌𝐄𝐍𝐓𝐈𝐎𝐍𝐁𝐎𝐓](https://github.com/SUKHPAL443/MAMBA_MENTIONBOT)\n"
        MAMBA_caption += f"║┣⪼𓆩༒𝓜𝓛𝓔𝓖𝓔𝓝𝓓༒𓆪⭆9.0.8,3.0\n"
        MAMBA_caption += f"║┣⪼𓆩༒𝓛𝓔𝓖𝓔𝓝𝓓𝓜𝓘𝓧༒𓆪⭆3.0\n"
        MAMBA_caption += f"║╰━━━━━━━━━━━━━━━➣ \n"
        MAMBA_caption += f"╔══❰𓆩༒𝐁𝐎𝐓 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍𓆩༒❱═➣\n"
        MAMBA_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        MAMBA_caption += f"║┣⪼𓆩༒𝓞𝓦𝓝𝓔𝓡༒𓆪⭆[𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"        
        MAMBA_caption += f"║┣⪼𓆩༒𝓢𝓣𝓐𝓣𝓤𝓢༒𓆪⭆𝐎𝐍𝐋𝐈𝐍𝐄\n"            
        MAMBA_caption += f"║┣⪼𓆩༒𝓑𝓞𝓣 𝓥𝓔𝓡𝓢𝓘𝓞𝓝༒𓆪⭆{mention}\n" 
        MAMBA_caption += f"║┣⪼𓆩༒𝓤𝓟𝓣𝓘𝓜𝓔༒𓆪⭆         {uptime}\n"
        MAMBA_caption += f"║┣⪼𓆩༒𝓑𝓞𝓣 𝓟𝓘𝓝𝓖༒𓆪⭆        290.087 \n"   
        MAMBA_caption += f"║┣⪼𓆩༒𝓜𝓐𝓜𝓑𝓐༒𓆪⭆         {MAMBAversion}\n"
        MAMBA_caption += f"║┣⪼𓆩༒𝓞𝓢:༒𓆪⭆    [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
        MAMBA_caption += f"║┣⪼𓆩༒𝓣𝓔𝓛𝓔𝓣𝓗𝓞𝓝༒𓆪⭆        {version.__version__}\n" 
        MAMBA_caption += f"║┣⪼[𓆩༒𝓜𝓐𝓜𝓑𝓐┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭༒𓆪](https://t.me/MAMBA_X_SUPPORT)\n"
        MAMBA_caption += f"║╰━━━━━━━━━━━━━━━➣ \n"
        MAMBA_caption += f"╚══════════════════❍⊱❁۪۪\n"
        
        await alive.client.send_file(
            alive.chat_id, MAMBA_IMG, caption=MAMBA_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"╔════❰𝓐𝓛𝓘𝓥𝓔 𝓛𝓘𝓝𝓤𝓧❱═❍⊱❁ \n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻    ┣⪼ [𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"
            f"║┣⪼𝓔-𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻  ┣⪼ [𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"
            f"║╰━━━━━━━━━━━━━━━➣\n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼𝓜𝓔𝓝𝓣𝓘𝓞𝓝𝓑𝓞𝓣    ┣⪼  [𝐌𝐄𝐍𝐓𝐈𝐎𝐍𝐁𝐎𝐓](https://github.com/SUKHPAL443/MAMBA_MENTIONBOT)\n"
            f"║┣⪼𝓜𝓛𝓔𝓖𝓔𝓝𝓓     ┣⪼9.0.8,3.0\n"
            f"║┣⪼𝓛𝓔𝓖𝓔𝓝𝓓𝓜𝓘𝓧    ┣⪼ 3.0\n"
            f"║╰━━━━━━━━━━━━━━━➣ \n"
            f"╔══❰🔥𝐁𝐎𝐓 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍🔥❱═➣\n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼𝓞𝓦𝓝𝓔𝓡      ┣⪼   [𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"
            f"║┣⪼𝓢𝓣𝓐𝓣𝓤𝓢       ┣⪼    𝐎𝐍𝐋𝐈𝐍𝐄\n"
            f"║┣⪼𝓑𝓞𝓣 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 ┣⪼  {mention}\n"
            f"║┣⪼𝓤𝓟𝓣𝓘𝓜𝓔       ┣⪼  {uptime}\n"
            f"║┣⪼𝓑𝓞𝓣 𝓟𝓘𝓝𝓖     ┣⪼   290.087 \n"   
            f"║┣⪼𝓜𝓐𝓜𝓑𝓐       ┣⪼  {MAMBAversion}\n"
            f"║┣⪼𝓞𝓢:          ┣⪼  [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
            f"║┣⪼𝓣𝓔𝓛𝓔𝓣𝓗𝓞𝓝      ┣⪼  {version.__version__}\n" 
            f"║┣⪼[✨🐍𝓜𝓐𝓜𝓑𝓐┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/MAMBA_X_SUPPORT)\n"
            f"║╰━━━━━━━━━━━━━━━➣ \n"
            f"╚══════════════════❍⊱❁۪۪\n"
        )


msg = f"""
  ⚜️ 𝓜𝓐𝓜𝓑𝓐 ιѕ σиℓιиє ⚜️
{Config.ALIVE_MSG}
f"╔════❰𝓐𝓛𝓘𝓥𝓔 𝓛𝓘𝓝𝓤𝓧❱═❍⊱❁ \n"
            **║╭━━━━━━━━━━━━━━━➣ \n"
            **┣⪼𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻    ┣⪼ [𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"
            **║┣⪼𝓔-𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻  ┣⪼ [𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"
            **║╰━━━━━━━━━━━━━━━➣\n"
            **║╭━━━━━━━━━━━━━━━➣ \n"
            **║┣⪼𝓜𝓔𝓝𝓣𝓘𝓞𝓝𝓑𝓞𝓣    ┣⪼  [𝐌𝐄𝐍𝐓𝐈𝐎𝐍𝐁𝐎𝐓](https://github.com/SUKHPAL443/MAMBA_MENTIONBOT)\n"
            **║┣⪼𝓜𝓛𝓔𝓖𝓔𝓝𝓓     ┣⪼9.0.8,3.0\n"
            **║┣⪼𝓛𝓔𝓖𝓔𝓝𝓓𝓜𝓘𝓧    ┣⪼ 3.0\n"
            **║╰━━━━━━━━━━━━━━━➣ \n"
            **╔══❰🔥𝐁𝐎𝐓 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍🔥❱═➣\n"
            **║╭━━━━━━━━━━━━━━━➣ \n"
            **║┣⪼𝓞𝓦𝓝𝓔𝓡      ┣⪼   [𝐌𝐀𝐌𝐁𝐀](t.me/BLACKMAMBA_OFFICIAL) \n"
            **║┣⪼𝓢𝓣𝓐𝓣𝓤𝓢       ┣⪼    𝐎𝐍𝐋𝐈𝐍𝐄\n"
            **║┣⪼𝓑𝓞𝓣 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 ┣⪼  {mention}\n"
            **║┣⪼𝓤𝓟𝓣𝓘𝓜𝓔       ┣⪼  {uptime}\n"
            **║┣⪼𝓑𝓞𝓣 𝓟𝓘𝓝𝓖     ┣⪼   290.087 \n"   
            **║┣⪼𝓜𝓐𝓜𝓑𝓐       ┣⪼  {MAMBAversion}\n"
            **║┣⪼𝓞𝓢:          ┣⪼  [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
            **║┣⪼𝓣𝓔𝓛𝓔𝓣𝓗𝓞𝓝      ┣⪼  {version.__version__}\n" 
            **║┣⪼[✨🐍𝓜𝓐𝓜𝓑𝓐┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/MAMBA_X_SUPPORT)\n"
            **║╰━━━━━━━━━━━━━━━➣ \n"
            **╚══════════════════❍⊱❁۪۪\n"
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def python_a(event):
    try:
        python = await bot.inline_query(botname, "alive")
        await python[0].click(event.chat_id)
        if event.sender_id == MAMBA_X_SUPPORT:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)

CmdHelp("alive").add_command(
    'bot', None, 'υѕє αи∂ ѕєє'
).add_type(
    "Official"
).add()
