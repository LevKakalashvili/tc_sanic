from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 5000
    AUTO_RELOAD: bool = True
    DB_URL: str = f"postgresql+psycopg2://{os.getenv('DB_NAME')}:{os.getenv('DB_USER_PSWD')}@{HOST}/{os.getenv('DB_NAME')}"
