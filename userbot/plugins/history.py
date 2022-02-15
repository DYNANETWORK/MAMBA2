from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from PYTHONBOT import bot, CmdHelp
from PYTHONBOT.utils import admin_cmd, edit_or_reply as eor, sudo_cmd

@PYTHONBOT.on(admin_cmd(pattern="history ?(.*)"))
@PYTHONBOT.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(PYTHONevent):
    if PYTHONevent.fwd_from:
        return 
    if not PYTHONevent.reply_to_msg_id:
       await eor(PYTHONevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await PYTHONevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(PYTHONevent, "Need actual users. Not Bots")
       return
    await eor(PYTHONevent, "Checking...")
    async with PYTHONevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await PYTHONevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(PYTHONevent, "User never changed his Username...")
          else: 
             await PYTHONevent.delete()
             await PYTHONevent.client.send_message(PYTHONevent.chat_id, response2.message)

@PYTHONBOT.on(admin_cmd(pattern="unh ?(.*)"))
@PYTHONBOT.on(sudo_cmd(pattern="unh ?(.*)", allow_sudo=True))
async def _(PYTHONevent):
    if PYTHONevent.fwd_from:
        return 
    if not PYTHONevent.reply_to_msg_id:
       await eor(PYTHONevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await PYTHONevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(PYTHONevent, "Need actual users. Not Bots")
       return
    await eor(PYTHONevent, "Checking...")
    async with PYTHONevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await PYTHONevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(PYTHONevent, "User never changed his Username...")
          else: 
             await PYTHONevent.delete()
             await PYTHONevent.client.send_message(LEGENDevent.chat_id, response3.message)

CmdHelp("history").add_command(
  "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
  "unh", "<reply to user>", "Fetches the Username History of replied users."
).add()
