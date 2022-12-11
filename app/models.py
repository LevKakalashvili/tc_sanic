import uuid

from passlib.hash import pbkdf2_sha256
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from typing_extensions import Self

from app.db import session
from app.validators import TransactionData

Base = declarative_base()


class Good(Base):
    __tablename__ = "good"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Numeric(5, 2), nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, price={self.price})"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.username}, admin={self.is_admin})"

    @classmethod
    def get_or_create(cls, username: str, password: str) -> Self:
        """Создание или получение пользователя."""
        new_user = session.query(User.username).filter_by(username=username).first()
        if new_user is None:
            new_user = User(username=username, password=pbkdf2_sha256.hash(password))
            session.add(new_user)
            session.commit()
        return new_user

    @classmethod
    def get(cls, username: str) -> Self:
        """Получение пользователя."""
        user = session.query(cls).filter_by(username=username).first()
        return user

    @classmethod
    def set_admins(cls, admins: list) -> bool:
        """Установка админов."""
        for user in session.query(cls).all():
            if user.username in admins:
                user.is_admin = True
            else:
                user.is_admin = False

        session.commit()
        return True

    def to_dict(self) -> dict:
        return {"user_id": self.id, "username": self.username}


class InactiveUser(Base):
    """Таблица не активированных пользователей."""

    __tablename__ = "inactive_user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    activation_link = Column(UUID(as_uuid=True), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.username})"

    @classmethod
    def get_or_create(cls, username: str, password: str) -> Self:
        """Создание или получение пользователя."""
        new_user = (
            session.query(InactiveUser.username, InactiveUser.activation_link)
            .filter_by(username=username)
            .first()
        )
        if new_user is None:
            new_user = InactiveUser(
                username=username,
                password=pbkdf2_sha256.hash(password),
                activation_link=uuid.uuid4(),
            )
            session.add(new_user)
            session.commit()
        return new_user

    @staticmethod
    def activate(activation_uuid: UUID) -> bool:
        """Копирует пользователя из временной таблицы для активации, в таблицу пользователей."""
        user = (
            session.query(InactiveUser).filter_by(activation_link=activation_uuid).one()
        )
        new_user = User(username=user.username, password=user.password)
        session.add(new_user)
        session.delete(user)
        session.commit()
        return True

    @staticmethod
    def clear() -> None:
        session.query(InactiveUser).delete()
        session.commit()


class Bill(Base):
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True)
    balance = Column(Numeric(5, 2), nullable=False)
    owner = Column(ForeignKey("user.id"), nullable=False)

    # transaction = Column(ForeignKey("transaction.id"), nullable=False)

    @classmethod
    def get_or_create_by_transaction(
        cls, transaction_data: TransactionData
    ) -> Self | None:
        bill = session.query(Bill).filter_by(id=transaction_data.bill_id).first()
        if bill is None:
            bill = Bill(
                id=transaction_data.bill_id,
                balance=0,
                owner=transaction_data.user_id,
            )
            session.add(bill)
            session.commit()
        return bill


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    # date = Column(DateTime, nullable=False)
    amount = Column(Numeric(5, 2), nullable=False)
    bill = Column(ForeignKey("bill.id"), nullable=False)
    signature = Column(String(50), nullable=False, unique=True)

    @classmethod
    def create(cls, transaction_data: TransactionData) -> Self | None:
        if (
            session.query(cls).filter_by(id=transaction_data.transaction_id).first()
            is None
        ):
            bill = Bill.get_or_create_by_transaction(transaction_data)
            bill.balance += transaction_data.amount
            transaction = Transaction(
                id=transaction_data.transaction_id,
                bill=bill.id,
                signature=transaction_data.signature,
                amount=transaction_data.amount,
            )
            session.add(transaction)
            session.commit()
            return transaction
        return None
