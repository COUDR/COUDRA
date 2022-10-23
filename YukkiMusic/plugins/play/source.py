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

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس كودرا","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/UUU_C_1",
        caption=f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝒔𝒐𝒖𝒓𝒄𝒆 𝒄𝒐𝒖𝒅𝒓𝒂 .](https://t.me/UUU_C_1)\n\n[❍ | 𝑪𝒐𝒖𝒅𝒓𝒂 𝒕𝒉𝒆 𝑩𝒆𝒔𝒕 𝒔𝒐𝒖𝒓𝒄𝒆 𝒐𝒏 𝒕𝒆𝒍𝒆 .
](https://t.me/UUU_C_1)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/UUU_C_1)\n\n||[❍ | 𝑪𝒐𝒖𝒅𝒓𝒂](https://t.me/COUDRA_1)||""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘾𝙤𝙪𝘿𝙧𝙖", url=f"https://t.me/COUDRA_1"), 
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝘾𝙊𝙐𝘿𝙍𝘼", url=f"https://t.me/UUU_C_1"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/MU_SIC_COUDRA_BOT?startgroup=true"),
                ],

            ]

        ),

    )
