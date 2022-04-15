from pyrogram.types import CallbackQuery
from pyrogram import Client

@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "next":
        await msg.message.edit("○○○○○")
        await msg.message.edit("●○○○○")
        await msg.message.edit("●●○○○")
        await msg.message.edit("●●●○○")
        await msg.message.edit("●●●●○")
        await msg.message.edit("●●●●●")
        await msg.message.edit(
            text=f" hello {msg.from_user.mention}  Start Text"
        )
