import json

from sanic import text
from sanic.views import HTTPMethodView
from sanic import json


from app.models import Good
from sqlalchemy import select
from app.db import session as db_session

class UserRegistration(HTTPMethodView):

    async def get(self, request):
        return text(f"You're here:  {request.method} - {request.server_path}")

    async def post(self, request):
        return text(f"You're here:  {request.method} - {request.server_path}")


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

