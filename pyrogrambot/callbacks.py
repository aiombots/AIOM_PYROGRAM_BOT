from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import Client
from pyrogrambot.buttons import MENU_BUTTON
import asyncio


@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "next":
        await msg.message.edit("○○○○○")
        await asyncio.sleep(0.9)
        await msg.message.edit("●○○○○")
        await asyncio.sleep(0.9)
        await msg.message.edit("●●○○○")
        await asyncio.sleep(0.9)
        await msg.message.edit("●●●○○")
        await asyncio.sleep(0.9)
        await msg.message.edit("●●●●○")
        await asyncio.sleep(0.9)
        await msg.message.edit("●●●●●")
        await asyncio.sleep(0.9)
        await msg.message.edit(
            text="Here Is You're Menu",
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )
    elif msg.data == "sticker":
        await msg.answer("Mode Chenged To Sticker")
        await msg.message.delete()
        await msg.message.reply_sticker(
            sticker="CAACAgIAAxkBAAECR5FiWgOUsaX2iRWuUtv8Y7AvIPoNuQAC-hAAAqHHKEg5ZXbrk1gHox4E",
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )

    elif msg.data == "video":
        await msg.answer("Mode Chenged To Video")
        await msg.message.delete()
        await msg.message.reply_video(
            video="https://telegra.ph/file/a976b6716470536985b5a.mp4",
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )

