import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("27461862"))
API_HASH = getenv("a3e9bdb30a6a2b9aaa667091a708be31")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7233484727:AAGQw_CW0E_a0E95EAq9MBQn-5jp5c5Z2cM")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://<villainmusic59>:<deathnote0p>@cluster0.t4v58.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002141133985))

# Get this value from @purvi_music_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5909658683))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Iamvillain77/Ods-Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iamvillain77")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/oldskoolgc")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @king_string_session_bot on Telegram
STRING1 = getenv("BQGjCOYAbxLMqWcOx7uDCptNMZbL6j8wTQ5fZGUTa7HjBep001JGXoFVk_IUvixhjIolvcyoPKoUccicN2qmX1GCEOFU8JlTvQV0FYfViFg5VKKcSy2jfXd1o0YCi41mS_h7vEGnJ1m39MErN6D5RwWMZ3h0BM1y1eEWHVO-roZedaCW20AvEMvLLtS3VGQUZnFY2Bf0BquQF_2XifUAXPYIZU0jfxP4p9txxgBNEB4SJlmM8etjBu6fGBM4Vmq-x1X6WMYZXB5N_-czn63rHHlfoEZWEC2MwVXTj4L26EJlu0fXJDONJWpP2KN2sD6q15fvs53S5RhsYbxfiBtFaXaZVLwjWQAAAAGhLtU7AA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/wrj4sw.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/wrj4sw.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/i493lf.jpg"
STATS_IMG_URL = "https://files.catbox.moe/wrj4sw.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
