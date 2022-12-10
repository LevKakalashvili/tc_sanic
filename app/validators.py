from decimal import Decimal

from sanic import request as request_type
from pydantic import BaseModel, ValidationError


class TransactionData(BaseModel):
    signature: str
    transaction_id: int
    user_id: int
    bill_id: int
    amount: Decimal


class UserData(BaseModel):
    username: str
    password: str


def check_userdata(request: request_type) -> UserData | None:
    try:
        return UserData(**request.json)
    except ValidationError:
        return None


def check_transaction_data(request: request_type) -> TransactionData | None:
    return TransactionData(**request.json)
