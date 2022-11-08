from dotenv import load_dotenv
import os

load_dotenv()


class AppSetting:
    DEBUG: bool = True,
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    AUTO_RELOAD: bool = True
    DB_URL: str = ""
    # DATABASE_URI = 'postgres+psycopg2://postgres:password@localhost:5432/books'


class DBSettings:
    DB_HOST: str = ""
    DB_PORT: int = ""
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_USER_PSWD: str = os.getenv("DB_USER_PSWD")
    DB_URL: str = ""
