from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogrambot.photos import KGF_PHOTOS
from pyrogrambot.buttons import KGF_D_BUTTON
import random

@Client.on_message(filters.regex("kgf 2") & filters.private)
async def kgf_filter(bot, message):
    await message.reply_photo(
        photo=random.choice(KGF_PHOTOS),
        reply_markup=InlineKeyboardMarkup(KGF_D_BUTTON)
    )

