import asyncio
from . import *
@bot.on(admin_cmd(pattern="happybirthday"))
async def _(event):
	await asyncio.sleep(1)
	await event.edit("""
▃▃▃▃▃▃▃▃▃▃▃
┊ ┊ ┊ ┊ ┊ ┊
┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩
┊ ┊ ┊ ✫
┊ ┊ ✧🎂🍰🍫🍭
┊ ┊ ✯
┊ . ˚ ˚✩
........♥️♥️..........♥️♥️_
.....♥️........♥️..♥️........♥️_
...♥️.............♥️............♥️
......♥️.....Happy.......♥️
...........♥️..............♥️
................♥️.....♥️
......................♥️
...............♥️........♥️
..........♥️...............♥️
.......♥️..Birthday....♥️_
.....♥️..........♥️...........♥️
.....♥️.......♥️_♥️.....♥️
.........♥️♥️........♥️♥️.....
.............................................
..... (¯`v´¯)♥️
.......•.¸.•´STAY BLESSED
....¸.•´      LOVE&FUN
... (   YOU DESERVE
☻/ THEM A LOT
/▌✿🌷✿
/ \     \|/\n▃▃▃▃▃▃▃▃▃▃▃
""")
CmdHelp("нαρϐιяτн").add_command(
	'happybirhtday', None, 'Use and See'
).add()

