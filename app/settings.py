from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DEBUG: bool = True
    HOST: str = os.getenv("DB_HOST")
    PORT: int = 5000
    AUTO_RELOAD: bool = True
    DB_URL: str = f"postgresql+psycopg2://" \
                  f"{os.getenv('DB_USER')}:" \
                  f"{os.getenv('DB_USER_PSWD')}@" \
                  f"{os.getenv('DB_HOST')}/" \
                  f"{os.getenv('DB_NAME')}"
