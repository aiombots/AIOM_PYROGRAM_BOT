from pyrogram import Client, filters
from pyrogrambot.photos import PHOTOS
from pyrogrambot.buttons import button
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
import random
import asyncio
FORCE_SUB = "AIOM_PYRO"

@Client.on_message(filters.command("start")) 
async def start_message(bot, message):
    await bot.send_chat_action(message.from_user.id, "Typing")
    await asyncio.sleep(2)
    if FORCE_SUB:
        try:
            user = await bot.get_chat_member(FORCE_SUB, message.chat.id)
            if user.status == "kicked out":
                await message.reply_text("<b>Aᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ 🚸</b>")
                return
        except UserNotParticipant:
             await message.reply_text(
                 text="Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ",
                 reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton(text="Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url="https://t.me/AIOM_PYRO") ]])
             )
             return
    await message.reply_photo(
        photo=random.choice(PHOTOS),
        caption=f"""Hᴇʟʟᴏ 👋, {message.from_user.mention}

Tʜɪs Is A Pʏʀᴏɢʀᴀᴍ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ Bʏ Tʜɪs Gᴜʏ

Cʜᴇᴄᴋ Oᴜᴛ Mʏ Fᴜᴛᴜʀᴇ's""",
        reply_markup=InlineKeyboardMarkup(button)
    )
