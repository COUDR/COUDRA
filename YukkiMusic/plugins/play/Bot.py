import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from config.config import START_IMG_URL

@app.on_message(
    command(["بوت"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG_URL}",
        caption=f"◍ [نعم ياقلب بوتك😍](https://t.me/UUU_C_1)\n√", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘿𝙚𝙑𝘾𝙤𝙪𝘿𝙧𝙖", url=f"https://t.me/COUDRA_1"), 
                ],[
                    InlineKeyboardButton(
                        "𝑺𝒐𝑼𝒓𝑪𝒆 𝑹𝒐𝑻𝒂𝑵𝒂", url=f"https://t.me/UUU_C_1"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/MU_SIC_COUDRA_BOT?startgroup=true"),
                ],
            ]
       ),
    ) 