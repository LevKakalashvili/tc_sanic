from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    ...


class Good(Base):
    ...


class UserAccount(Base):
    ...


class Transaction(Base):
    ...
