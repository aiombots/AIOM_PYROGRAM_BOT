from pyrogram import Client

Pyrogrambot = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    plugins=dict(root="pyrogrambot")
)

Pyrogrambot.run()
