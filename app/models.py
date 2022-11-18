from sqlalchemy import Column, Integer, Numeric, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Good(Base):
    __tablename__ = "good"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Numeric(5, 2), nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, price={self.price})"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"User(id={self.id}, name={self.username}, price={self.is_admin})"


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    balance = Column(Numeric(5, 2), nullable=False)
    owner = Column(ForeignKey("user.id"), nullable=False)


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    amount = Column(Numeric(5, 2), nullable=False)
    account = Column(ForeignKey("account.id"), nullable=False)
