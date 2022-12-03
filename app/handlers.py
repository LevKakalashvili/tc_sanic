import json
from uuid import UUID

from sanic import exceptions, json, redirect
from sanic.views import HTTPMethodView
from sqlalchemy import select

from app.db import session as db_session
from app.models import Good, User, InactiveUser
from app.validators import check_credentials
from app.urls import Urls


class UserActivation(HTTPMethodView):
    async def get(self, request, activation_link: UUID):
        if InactiveUser.activate(activation_uuid=activation_link):
            return json({"success": True,
                         "message": "User has been activated."})
        return json({"success": False,
                     "message": "User hasn't been activated."})


class UserRegistration(HTTPMethodView):

    async def post(self, request):
        if not check_credentials(request):
            return json({"success": False,
                         "message": "No user data: user name and/or password."})

        if User.get(username=request.credentials.username) is None:
            inactive_user = InactiveUser.get_or_create(username=request.credentials.username,
                                                       password=request.credentials.password)
            return json({"success": True,
                         "activation_link": f"{request.scheme}://"
                                            f"{request.host}"
                                            f"{Urls.USER_ACTIVATION}/"
                                            f"{inactive_user.activation_link}"}
                        )
        else:
            return json({"success": False,
                         "message": "User with this name already exists."})


class GoodsList(HTTPMethodView):

    async def get(self, request):
        json_data = []
        goods = select(Good)
        for good in db_session.scalars(goods):
            json_data.append(
                {
                    "name": good.name,
                    "price": str(good.price)
                }
            )
        return json({"goods": json_data})
