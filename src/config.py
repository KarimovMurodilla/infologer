from environs import Env

env = Env()
env.read_env()

DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")
DB_NAME = env.str("DB_NAME")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

TESTING = env.bool("TESTING")
DB_HOST_TEST = env.str("DB_HOST_TEST")
DB_PORT_TEST = env.str("DB_PORT_TEST")
DB_NAME_TEST = env.str("DB_NAME_TEST")
DB_USER_TEST = env.str("DB_USER_TEST")
DB_PASS_TEST = env.str("DB_PASS_TEST")
DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

REDIS_HOST = env.str("REDIS_HOST")
REDIS_PORT = env.str("REDIS_PORT")

SECRET = env.str("SECRET")
FRONTEND_BASE_URL = env.str("FRONTEND_BASE_URL")

# ---Mailjet Api (Send mail)---
API_KEY_EMAIL = env.str("API_KEY_EMAIL")
API_SECRET = env.str("API_SECRET")

# Email Sender
SENDER_GMAIL = env.str("SENDER_GMAIL")
SENDER_NAME = env.str("SENDER_NAME")

# Google Oauth2
CLIENT_ID = env.str("CLIENT_ID")
CLIENT_SECRET = env.str("CLIENT_SECRET")