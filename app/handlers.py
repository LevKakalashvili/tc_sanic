"""Описание всех хэндлеров."""
import json
from uuid import UUID

from sanic import json
from sanic.views import HTTPMethodView
from sanic_jwt import protected
from sqlalchemy import select

from app.db import session as db_session
from app.models import Good, InactiveUser, Transaction as Transaction_, User
from app.urls import Urls
from app.validators import check_transaction_data, check_userdata


class UserActivation(HTTPMethodView):
    """Активация пользователя."""

    async def get(self, request, activation_link: UUID):
        if InactiveUser.activate(activation_uuid=activation_link):
            return json({"success": True, "message": "User has been activated."})
        return json({"success": False, "message": "User hasn't been activated."})


class UserRegistration(HTTPMethodView):
    """Регистрация пользователя."""

    async def post(self, request):
        user_data = check_userdata(request)
        if user_data is None:
            return json(
                {"success": False, "message": "No user data: username and/or password."},
            )

        if User.get(username=user_data.username) is None:
            inactive_user = InactiveUser.get_or_create(
                username=user_data.username, password=user_data.password,
            )
            return json(
                {
                    "success": True,
                    "activation_link": f"{request.scheme}://"
                    f"{request.host}"
                    f"{Urls.USER_ACTIVATION}/"
                    f"{inactive_user.activation_link}",
                },
            )
        else:
            return json(
                {"success": False, "message": "User with this name already exists."},
            )


class GoodsList(HTTPMethodView):
    """Список товаров."""

    async def get(self, request):
        # TODO перенести в models
        json_data = []
        goods = select(Good)
        for good in db_session.scalars(goods):
            json_data.append({"name": good.name, "price": str(good.price)})
        return json({"success": False, "goods": json_data})


class Transaction(HTTPMethodView):
    """Добавление транзакции."""

    decorators = [protected()]

    async def post(self, request):
        transaction_data = check_transaction_data(request)
        transaction = Transaction_.create(transaction_data)
        if transaction is None:
            json({"success": False, "message": "Transaction is incorrect"})
        return json({"success": True, "message": "Transaction has been add"})
