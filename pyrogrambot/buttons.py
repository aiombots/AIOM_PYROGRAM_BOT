from pyrogram.types import InlineKeyboardButton

button = [[
         InlineKeyboardButton("Mᴇɴᴜ", callback_data="next")
         ]]

MENU_BUTTON = [[
              InlineKeyboardButton("Sᴛɪᴄᴋᴇʀ", callback_data="sticker"),
              InlineKeyboardButton("Vɪᴅᴇᴏ", callback_data="video")
              ],[
              InlineKeyboardButton("Pʜᴏᴛᴏ", callback_data="photo"),
              InlineKeyboardButton("Dᴇᴛᴀɪʟs", callback_data="id")
              ],[
              InlineKeyboardButton("Mᴏᴠɪᴇs", callback_data="movies"),
              InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
              ],[
              InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="back"),
              InlineKeyboardButton("Cᴏᴍᴍᴀɴᴅs", callback_data="commands")
              ]]

MOVIE_BUTTON = [[
               InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="next")
               ]]
