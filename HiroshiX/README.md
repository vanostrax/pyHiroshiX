<h2> pyHiroshiX by HiroshiX </h2>

pyHiroshiX is pyrogram based pip module for smooth functioning of telegram bots


<h3> Example! </h3>

``` python
from HiroshiX.functions import promote_user
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("promote"))
async def promote_(Client, Message):
   """Syntax: /promote <user (user's ID or username)> <tag (optional)> """
   await promote_user(Client, Message)
```



