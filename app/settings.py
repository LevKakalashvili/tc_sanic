from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DEBUG = True
    HOST = os.getenv("DB_HOST")
    PORT = 5000
    AUTO_RELOAD = True
    DB_URL = (
        f"postgresql+psycopg2://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_USER_PSWD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )
    INACTIVE_USER_CLEAR_CRON = "59 23 * * *"  # каждый день в 23.59
    ADMINS_LIST = [
        "user_1",
        "user_2",
    ]
    JWT_SECRET = os.getenv("JWT_SECRET")
