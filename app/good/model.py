from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Good(Base):
    __tablename__ = "good"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    price = Column(Numeric(5, 2), nullable=True)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, price={self.price!r})"
