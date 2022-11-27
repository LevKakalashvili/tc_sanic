from sqlalchemy import Column, Integer, Numeric, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from passlib.hash import pbkdf2_sha256

Base = declarative_base()
from app.db import session


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
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    is_admin = Column(Boolean, default=False)
    is_activated = Column(Boolean, default=False)

    def __repr__(self):
        return f"User(id={self.id}, name={self.username}, admin={self.is_admin})"

    @staticmethod
    def create(username: str, password: str) -> str:
        """Создания пользователя."""
        if session.query(User.username).filter_by(username=username).first() is None:
            new_user = User(
                    username=username,
                    password=pbkdf2_sha256.hash(password)
                )
            session.add(new_user)
            url = "/activation_url"
        else:
            url = "/user_exists"
        session.commit()
        return url


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
