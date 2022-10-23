import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["ألمطور","كودرا","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/COUDRA_1",
        caption=f"""◍ الزرار الاول: قناه السورس \n◍ الزرار الثاني: هو مبرمج السورس\n√""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "𝑺𝒐𝑼𝒓𝑪𝒆 𝑹𝒐𝑻𝒂𝑵𝒂", url=f"https://t.me/UUU_C_1"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "𝘿𝙚𝙑 𝘾𝙤𝙪𝘿𝙧𝙖", url=f"https://t.me/COUDRA_1"),
                ],
            ]
        ),
    )
