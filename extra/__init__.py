

# [Telethon || Red7 scanner]
from telethon.tl import types, functions
from PhoenixScanner import Phoenix

RIGHTS = types.ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

def update_scanlist(Red7):
   newlist = Red7.scanlist()
   if newlist == {'message': 'Invalid Token'}:
      newlist = Red7.scanlist()
      if newlist == {'message': 'Invalid Token'}:
         raise 'Invalid Scanner Token'
   return newlist

async def Red7_Watch_telethon(HiroshiX, message):
   user = message.sender_id
   Red7_Client = Phoenix("RED7-riw5wtg5mpjlcxi6jtjqhh")
   msg = f"""
 Alert ⚠️
User [{user}](tg://user?id={user}) is officially
Scanned by Team Red7 | Phoenix API ;)

Appeal [Here](https://t.me/Red7WatchSupport)
   """
   try:
      try:
         check = Red7_Client.check(user)
         if check['is_gban']:
            try:
                await HiroshiX(functions.channels.EditBannedRequest(message.chat_id, user, BANNED_RIGHTS))
            except BaseException:
                pass
            await HiroshiX.send_message(message.chat_id, msg, link_preview=False)
      except:
         SCANLIST = []
         SCANLIST = update_scanlist(Red7_Client)
         if user in SCANLIST:
            try:
                await HiroshiX(functions.channels.EditBannedRequest(message.chat_id, user, BANNED_RIGHTS))
            except BaseException:
                pass
            await HiroshiX.send_message(message.chat_id, msg, link_preview=False)
   except Exception as error:
      print(str(error))


""" Some Telethon functions """
async def get_user_telethon(message):
    try:
        args = message.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        args = None
    if message.reply_to_msg_id:
        previous_message = await message.get_reply_message()
        user = await message.client.get_entity(previous_message.sender_id)
        extra = "".join(args) if args else ""
    elif args:
        extra = None
        x = args[0]
        if len(args) == 2:
            extra = args[1]
        if x.isnumeric():
            x = int(x)
        if not x:
            await message.reply("I don't know who you're talking about, you're going to need to specify a user...!")
            return
        try:
            x = await message.client.get_entity(x)
        except (TypeError, ValueError):
            await message.reply("Looks like I don't have control over that user, or the ID isn't a valid one. If you reply to one of their messages, I'll be able to interact with them.")
            return
    else:
        await message.reply("I don't know who you're talking about, you're going to need to specify a user...!")
        return
    return user, extra
