from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import Client
from pyrogrambot.photos import PHOTOS
import random
from pyrogrambot.buttons import MENU_BUTTON
import asyncio


@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "next":
        await msg.message.edit("○○○○○")
        asyncio.sleep(0.9)
        await msg.message.edit("●○○○○")
        asyncio.sleep(0.9)
        await msg.message.edit("●●○○○")
        asyncio.sleep(0.9)
        await msg.message.edit("●●●○○")
        asyncio.sleep(0.9)
        await msg.message.edit("●●●●○")
        asyncio.sleep(0.9)
        await msg.message.edit("●●●●●")
        asyncio.sleep(0.9)
        await msg.message.edit(
            photo=random.choice(PHOTOS),
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )
    elif msg.data == "sticker":
        await msg.message.edit(
            sticker="CAACAgIAAxkBAAECR5FiWgOUsaX2iRWuUtv8Y7AvIPoNuQAC-hAAAqHHKEg5ZXbrk1gHox4E",
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )
