import os
from telethon import TelegramClient, events
#
# Burayı gurcalama
# 
# 
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
bot_username = os.environ.get("BOT_USERNAAME")
owner_username = os.environ.get("OWNER_USERNAAME")
