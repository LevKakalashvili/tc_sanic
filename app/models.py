import uuid

from passlib.hash import pbkdf2_sha256
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, delete
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

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

    def __repr__(self):
        return f"User(id={self.id}, name={self.username}, admin={self.is_admin})"

    @staticmethod
    def get_or_create(username: str, password: str) -> object:
        """Создание или получение пользователя."""
        new_user = session.query(User.username).filter_by(username=username).first()
        if new_user is None:
            new_user = User(
                username=username,
                password=pbkdf2_sha256.hash(password)
            )
            session.add(new_user)
            session.commit()
        return new_user

    @staticmethod
    def get(username: str) -> object | None:
        """Получение пользователя."""
        user = session.query(User.username).filter_by(username=username).first()
        return user

    @classmethod
    def update_admins(cls, admins: list):
        for user in session.query(cls).all():
            if user.username in admins:
                user.is_admin = True
            else:
                user.is_admin = False

        session.commit()
        return True


class InactiveUser(Base):
    """Таблица не активированных пользователей."""
    __tablename__ = "inactive_user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    activation_link = Column(UUID(as_uuid=True), nullable=False, unique=True)

    def __repr__(self):
        return f"User(id={self.id}, name={self.username})"

    @staticmethod
    def get_or_create(username: str, password: str) -> object:
        """Создание или получение пользователя."""
        new_user = session.query(InactiveUser.username, InactiveUser.activation_link).filter_by(
            username=username).first()
        if new_user is None:
            new_user = InactiveUser(
                username=username,
                password=pbkdf2_sha256.hash(password),
                activation_link=uuid.uuid4()
            )
            session.add(new_user)
            session.commit()
        return new_user

    @staticmethod
    def activate(activation_uuid: UUID) -> bool:
        """Копирует пользователя из временной таблицы для активации, в таблицу пользователей."""
        user = session.query(InactiveUser).filter_by(activation_link=activation_uuid).one()
        new_user = User(
            username=user.username,
            password=user.password
        )
        session.add(new_user)
        session.delete(user)
        session.commit()
        return True

    @staticmethod
    def clear():
        session.query(InactiveUser).delete()
        session.commit()


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
