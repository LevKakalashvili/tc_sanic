from sanic import Sanic, text
from app.settings import Config as app_config
from app.db import db_engine
from app.handlers import UserRegistration, GoodsList

app = Sanic("test_sanic_app")
app.ctx.db_engine = db_engine
# app.blueprint(user, url_prefix="/user")

# def hello_world_1(request):
#     return text("Hello, world 11111.")


# @app.get("/")
# async def hello_world(request):
#     return text("Hello, world.")
#
# app.add_route(UserRegistration.as_view(), "/user/registration")
app.add_route(UserRegistration.as_view(), UserRegistration().uri)
app.add_route(GoodsList.as_view(), "/good/all")

# def setup_database():
#     @app.listener("after_server_start")
#     async def connect_to_db(*args, **kwargs):
#         app.ctx.db_engine =
#         )
#         await app.ctx.db_engine.connect()

    # @app.listener('after_server_stop')
    # async def disconnect_from_db(*args, **kwargs):
    #     print(app.router.routes_all)
    #     # await app.db.disconnect()


def init():
    # setup_database()
    if app_config.DEBUG:
        app.run(
            debug=app_config.DEBUG,
            host=app_config.HOST,
            port=app_config.PORT,
            auto_reload=app_config.AUTO_RELOAD,
        )
    else:
        app.run()


if __name__ == "__main__":
    init()
