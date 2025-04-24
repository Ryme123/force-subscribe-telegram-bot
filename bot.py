import logging
from pyrogram import Client
from Config import Config

logging.basicConfig(level=logging.INFO)

plugins = dict(
    root="plugins",
    include=[
        "forceSubscribe",
        "help"
    ]
)

app = Client(
     'ForceSubscribe',
      bot_token = Config.BOT_TOKEN,
      api_id =19259149 Config.APP_ID,
      api_hash = 67e9ed15eb0adf9d3b391311933fa594 Config.API_HASH,
      plugins = plugins
)

app.run()
