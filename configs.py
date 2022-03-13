import os
from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))


class Var(object):
         APP_ID = int(os.environ.get("APP_ID", 0))
         API_HASH = os.environ.get("API_HASH", "")
         TOKEN = os.environ.get("TOKEN", "")
         BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
