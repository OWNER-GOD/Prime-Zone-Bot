import os
from typing import List

API_ID = int(os.getenv("API_ID", "21769517"))
API_HASH = os.getenv("API_HASH", "a18bca05e643355610f88e15425287a7")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://desembermethod_db_user:v4ADkgywaYxrZW1y@cluster0.ghvofhb.mongodb.net/?appName=Cluster0")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", "-1003624112121"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "7562079827"))
PICS = (os.environ.get("PICS", "")).split()
LOG_CHNL = int(os.getenv("LOG_CHNL", "-1003629003804"))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "BYGOD_HELPER") # Without @
IS_FSUB = bool(os.environ.get("FSUB", False))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_LOG", "-1003618791775"))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "240"))
