from sqlalchemy import create_engine
from sqlalchemy.orm import Session

db_engine = create_engine("postgresql+psycopg2://", echo=True, future=True)

session = Session(db_engine)