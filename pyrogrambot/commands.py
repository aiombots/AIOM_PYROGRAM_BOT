from pyrogram import Client, filters

@Client.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(PHOTOS),
        caption=f"""Hᴇʟʟᴏ 👋, {message.from_user.mention}

Tʜɪs Is A Pʏʀᴏɢʀᴀᴍ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ Bʏ Tʜɪs Gᴜʏ

Cʜᴇᴄᴋ Oᴜᴛ Mʏ Fᴜᴛᴜʀᴇ's""",
        reply_markup=InlineKeyboardMarkup(button)
    )
