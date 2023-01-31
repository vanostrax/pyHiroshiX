<p align="center">
   <a href="https://github.com/HiroshiX">
      <img src="HiroshiX/data/asoyy.jpg" alt="HiroshiX" width="300" aligne='centre'>
   </a>
</p>
<h1 align="center">
   <b> pyHiroshiX </b> <br>  

</h1>

 * [![PyPI - Version](https://img.shields.io/pypi/v/pyHiroshiX?style=round)](https://pypi.org/project/pyHiroshiX) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyHiroshiX?label=DOWNLOADS&style=round)](https://pypi.org/project/pyHiroshiX) 

----

<b>About:</b> pyHiroshiX have many useful functions, that you can use in your repos/repostory. It'll make you code/bot smooth and fast!

<h4> Installation </h4>

```python 
pip3 install pyHiroshiX
```

<h4> Import functions </h4>

``` python
from HiroshiX.functions import <functions name>
```

<h4> Functions available: </h4>

 > [Click Here](https://github.com/vanostrax/pyHiroshiX/tree/main/HiroshiX/functions#-functions-available-) </b> 

<h3> Example. </h3>

``` python
from HiroshiX.functions import ban_user
from pyrogram import Client, filters 
from pyrogram.types import Message


@Client.on_message(filters.command("ban"))
async def ban_(client, message):
   await ban_user(client, message)
```
