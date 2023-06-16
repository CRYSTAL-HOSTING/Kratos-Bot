import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

OWNER_ID = int(os.environ.get("OWNER_ID", ""))

PORT = os.environ.get("PORT", "8080")

DB_URI = os.environ.get("DATABASE_URL", "")

DB_NAME = os.environ.get("DATABASE_NAME", "")

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001216650755"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention} 👋\n\n• Join Our Channel To Get Access To Files Through Links !\n\n🔰: @Crystal_Games\n🗨️: @Crystal_Games_Discussion</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>🗣️ Kratos:\nHello {mention} 👋\nYou Need To Join Our Channel, So You Can Access My Links !\n\n🔰: @Crystal_Games\n🗨️: @Crystal_Games_Discussion</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "🤖 <b>BOT UPTIME</b> 📊\n\n ⏳: {uptime}"
USER_REPLY_TEXT = "🔔 <b>Telegram Notification</b>:\n\nKratos Is Going In a War ⚔️, So He Can't Talk To You !\n\nYou Can Type /start For Help !\n\n🔰: @Crystal_Games\n🗨️: @Crystal_Games_Discussion\n\n👀: bit.ly/3NyZN5W"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "KratosDiary.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
