import json

from sanic import text
from sanic.views import HTTPMethodView


from app.models import Good
from sqlalchemy import select
from app.db import session as db_session


class User(HTTPMethodView):
    USER_URI = "/user"


class UserRegistration(User):

    def __init__(self):
        super(User, self).__init__()
        self.uri = f"{self.USER_URI}/registration"

    async def get(self, request):
        return text(f"You're here:  {request.method} - {request.server_path}")

    async def post(self, request):
        return text(f"You're here:  {request.method} - {request.server_path}")


class GoodsList(HTTPMethodView):

    async def get(self, request):
        json_data = []
        goods = select(Good)
        for good in db_session.scalar(goods):
            json_data.append(
                {
                    "id": good.id,
                    "name": good.name,
                    "price": good.price
                }
            )
        return json.dumps({"Товары": json_data})

