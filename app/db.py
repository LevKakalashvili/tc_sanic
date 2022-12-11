"""Модуль подключения к БД."""
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.settings import Config as AppConfig

db_engine: Engine = create_engine(
    AppConfig.DB_URL, echo=AppConfig.DEBUG,
)

session = Session(db_engine)
