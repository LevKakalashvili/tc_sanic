import json

from sanic import exceptions, json, redirect
from sanic.views import HTTPMethodView
from sqlalchemy import select

from app.db import session as db_session
from app.models import Good, User


class UserRegistration(HTTPMethodView):

    async def post(self, request):
        # if not validator:
        #     redirect

        if getattr(request, "credentials") is not None \
                and (request.credentials.username and request.credentials.password):
            redirect_url = User.create(username=request.credentials.username,
                                       password=request.credentials.password)
        else:
            raise exceptions.NotFound("No user data: user name and/or password.")

        return redirect(redirect_url)


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
