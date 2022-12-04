from sqlalchemy import create_engine

from app.settings import Config as AppConfig
from sqlalchemy.orm import Session

db_engine = create_engine(AppConfig.DB_URL, echo=True if AppConfig.DEBUG == "True" else False)

session = Session(db_engine)
