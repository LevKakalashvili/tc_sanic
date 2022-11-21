from sqlalchemy import create_engine
from app.settings import Config as app_config
from sqlalchemy.orm import Session

db_engine = create_engine(app_config.DB_URL, echo=True if app_config.DEBUG == "True" else False)

session = Session(db_engine)