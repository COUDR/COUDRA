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
        caption=f"◍ [نعم ياقلب بوتك😍](https://t.me/XxvprxX)\n√", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=_["المطور🏂"], user_id=OWNER
                ],
                [     
                    InlineKeyboardButton(
                        text=_["اضف البوت الي مجموعتك✅"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                ],
            ]
        ),
    )
