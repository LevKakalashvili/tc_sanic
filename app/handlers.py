import json

from sanic import text
from sanic.views import HTTPMethodView
from sqlalchemy.orm import Session

from app.models import Good
from sqlalchemy import select
from app.main import app

session = Session(app.ctx.db)

# class User(HTTPMethodView):
#     def __ini__(self):
#         self.endpoint = "/user"


# class UserRegistration(User):
class UserRegistration(HTTPMethodView):

    # def __ini__(self):
    #     self.endpoint = f"{super.endpoint}/registration"
    #     super(User, self).__ini__()

    async def get(self, request):
        return text(f"You're here:  {request.method} - {request.server_path}")

    async def post(self, request):
        return text(f"You're here:  {request.method} - {request.server_path}")


class GoodsList(HTTPMethodView):

    async def get(self, request):

        json_data = []
        goods = select(Good)
        for good in session.scalar(goods):
            json_data.append(
                {
                    "id": good.id,
                    "name": good.name,
                    "price": good.price
                }
            )
        return json.dump({"Товары": json_data})
