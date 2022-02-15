from telethon.sync import TelegramClient
from telethon.sessions import StringSession

MAMBABOT = """
"""
print(MAMBABOT)
print(
    """String Generator. ==> Mambabot. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly.

╭━╮╭━┳━━━┳━╮╭━┳━━╮╭━━━╮
┃┃╰╯┃┃╭━╮┃┃╰╯┃┃╭╮┃┃╭━╮┃
┃╭╮╭╮┃┃╱┃┃╭╮╭╮┃╰╯╰┫┃╱┃┃
┃┃┃┃┃┃╰━╯┃┃┃┃┃┃╭━╮┃╰━╯┃
┃┃┃┃┃┃╭━╮┃┃┃┃┃┃╰━╯┃╭━╮┃
╰╯╰╯╰┻╯╱╰┻╯╰╯╰┻━━━┻╯╱╰╯
╭━━╮╭━━━┳━━━━╮MAMBA
┃╭╮┃┃╭━╮┃╭╮╭╮┃
┃╰╯╰┫┃╱┃┣╯┃┃╰╯
┃╭━╮┃┃╱┃┃╱┃┃
┃╰━╯┃╰━╯┃╱┃┃
╰━━━┻━━━╯╱╰╯SUKHPAL_KHERERA""")
print("Real stick Mamba newlock")
APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as MAMBA:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(MAMBABOT.session.save())
    print("")
    print(
        "You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions."
    )
    omk = MAMBABOT.send_message("me", f"`{MAMBABOT.session.save()}`")
    omk.reply(
        "The above is the `MAMBA_STRING` [MAMBABOT](https://t.me/MAMBA_X_SUPPORT)"
    )
