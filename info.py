# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')

# Bot Information
SESSION = environ.get('SESSION', 'SKR')
API_ID = int(environ.get('API_ID', '20196547'))
API_HASH = environ.get('API_HASH', 'f1d32b4f43d2e1d50b863b1a77ddf2a2')
BOT_TOKEN = environ.get('BOT_TOKEN', '7148889388:AAEb44UtdP2xPP5yLIIIit1eQJinkc3ZE9Y')

# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1315244338').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else ADMINS

# Start message images
PICS = environ.get('PICS', 'https://telegra.ph/file/5924d32cbdc949f7df047-64dc1f885fdbc5b102.jpg').split()

# Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001992530532'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
REQUEST_TO_JOIN_MODE = environ.get('REQUEST_TO_JOIN_MODE', 'False').lower() == 'true'
TRY_AGAIN_BTN = environ.get('TRY_AGAIN_BTN', 'False').lower() == 'true'

auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

reqst_channel = environ.get('REQST_CHANNEL', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None

INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

import re
from os import environ

# Pattern to identify numeric Telegram IDs
id_pattern = re.compile(r"^-?\d+$")

import re

id_pattern = re.compile(r"^-?\d+$")

# For File Store Channel (must be a **single** int ID)
FILE_STORE_CHANNEL = int(environ.get('FILE_STORE_CHANNEL', '-1002575745911'))

# For Delete Channels (can be a mix of usernames and IDs)
DELETE_CHANNELS = [
    int(dch) if id_pattern.match(dch) else dch
    for dch in environ.get('DELETE_CHANNELS', '-1002574075732').split()
]


# MongoDB Info
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://...")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'SKR_updates')
O_DB_URI = environ.get('O_DB_URI', "")
F_DB_URI = environ.get('F_DB_URI', "")
S_DB_URI = environ.get('S_DB_URI', "")

# Premium/Referral
PREMIUM_AND_REFERAL_MODE = environ.get('PREMIUM_AND_REFERAL_MODE', 'False').lower() == 'true'
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs...</b>')

# Clone Mode
CLONE_MODE = environ.get('CLONE_MODE', 'False').lower() == 'true'
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "")
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '')

# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/kdkkdkosoibzu')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/kdkkdkosoibzu')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'kdkkdkosoibzu')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/kdkkdkosoibzu')

# Boolean Flags
def str2bool(v): return str(v).lower() in ("yes", "true", "t", "1")

AI_SPELL_CHECK = str2bool(environ.get('AI_SPELL_CHECK', 'True'))
PM_SEARCH = str2bool(environ.get('PM_SEARCH', 'True'))
BUTTON_MODE = str2bool(environ.get('BUTTON_MODE', 'True'))
MAX_BTN = str2bool(environ.get('MAX_BTN', 'True'))
IS_TUTORIAL = str2bool(environ.get('IS_TUTORIAL', 'True'))
IMDB = str2bool(environ.get('IMDB', 'True'))
AUTO_FFILTER = str2bool(environ.get('AUTO_FFILTER', 'True'))
AUTO_DELETE = str2bool(environ.get('AUTO_DELETE', 'True'))
LONG_IMDB_DESCRIPTION = str2bool(environ.get('LONG_IMDB_DESCRIPTION', 'True'))
SPELL_CHECK_REPLY = str2bool(environ.get('SPELL_CHECK_REPLY', 'True'))
MELCOW_NEW_USERS = str2bool(environ.get('MELCOW_NEW_USERS', 'True'))
PROTECT_CONTENT = str2bool(environ.get('PROTECT_CONTENT', 'False'))
PUBLIC_FILE_STORE = str2bool(environ.get('PUBLIC_FILE_STORE', 'True'))
NO_RESULTS_MSG = str2bool(environ.get('NO_RESULTS_MSG', 'True'))
USE_CAPTION_FILTER = str2bool(environ.get('USE_CAPTION_FILTER', 'True'))

# Token Verification
VERIFY = str2bool(environ.get('VERIFY', 'False'))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')
VERIFY_SECOND_SHORTNER = str2bool(environ.get('VERIFY_SECOND_SHORTNER', 'False'))
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')

# Shortlink
SHORTLINK_MODE = str2bool(environ.get('SHORTLINK_MODE', 'False'))
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
TUTORIAL = environ.get('TUTORIAL', '')

# Misc
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Hello My De Friends From SKR ❤️')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", script.CAPTION)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE_TXT)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Filter Settings
LANGUAGES = ["malayalam", "mal", "tamil", "tulu", "english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = [f"season {i}" for i in range(1, 11)]
EPISODES = [f"E{i:02d}" for i in range(1, 41)]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = [str(y) for y in range(1900, 2026)]

# Online Stream
STREAM_MODE = str2bool(environ.get('STREAM_MODE', 'True'))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "https://your-app.herokuapp.com/")

# Rename & Auto Approve
RENAME_MODE = str2bool(environ.get('RENAME_MODE', 'True'))
AUTO_APPROVE_MODE = str2bool(environ.get('AUTO_APPROVE_MODE', 'False'))

# Reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# Handle Multiple DBs
MULTIPLE_DATABASE = bool(O_DB_URI or F_DB_URI or S_DB_URI)

if not MULTIPLE_DATABASE:
    USER_DB_URI = OTHER_DB_URI = FILE_DB_URI = SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = O_DB_URI
    FILE_DB_URI = F_DB_URI
    SEC_FILE_DB_URI = S_DB_URI
    
    # File size & rename settings
MAX_FILE_SIZE = int(environ.get("MAX_FILE_SIZE", "2097152000"))  # ~2GB
ALLOW_UPLOAD_TO_PVT = str2bool(environ.get('ALLOW_UPLOAD_TO_PVT', 'True'))
ALLOW_UPLOAD_TO_CHANNEL = str2bool(environ.get('ALLOW_UPLOAD_TO_CHANNEL', 'True'))
IS_CAPTION_FILTER = str2bool(environ.get('IS_CAPTION_FILTER', 'True'))

# Optional Logging (For Dev/Debug Mode)
ENABLE_LOGGING = str2bool(environ.get("ENABLE_LOGGING", "True"))
LOG_LEVEL = environ.get("LOG_LEVEL", "INFO")  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Worker count for aiohttp or uvicorn/gunicorn setups
WORKERS = int(environ.get("WORKERS", "4"))

# User limits
DAILY_UPLOAD_LIMIT = int(environ.get("DAILY_UPLOAD_LIMIT", "10"))  # In GB or file count based on logic
USER_MAX_FILE_LIMIT = int(environ.get("USER_MAX_FILE_LIMIT", "5"))

# Safe Mode
SAFE_MODE = str2bool(environ.get("SAFE_MODE", "False"))

# Debug Mode Printout
if ENABLE_LOGGING:
    import logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    )
    logging.info("Bot configuration loaded successfully.")

# Print important ENV summary if in debug/dev
if ENABLE_LOGGING and LOG_LEVEL.upper() == "DEBUG":
    print(f"SESSION: {SESSION}")
    print(f"API_ID: {API_ID}")
    print(f"BOT_TOKEN: {BOT_TOKEN[:10]}...")  # Hide full token
    print(f"ADMINS: {ADMINS}")
    print(f"AUTH_USERS: {AUTH_USERS}")
    print(f"LOG_CHANNEL: {LOG_CHANNEL}")
    print(f"DB: {DATABASE_URI}")
    print(f"SHORTLINK_MODE: {SHORTLINK_MODE}, VERIFY: {VERIFY}")
    print("ENV loaded completely and validated.")

# Don't Remove This Line
# Credit: @VJ_Botz | YouTube: @Tech_VJ | Telegram: @KingVJ01