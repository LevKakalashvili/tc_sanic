from sanic import Sanic, text
from app.settings import Config as app_config
from sqlalchemy import create_engine

from app.user.auth import user

app = Sanic("test_sanic_app")

app.blueprint(user, url_prefix="/user")

# def hello_world_1(request):
#     return text("Hello, world 11111.")
#
#
# @app.get("/")
# async def hello_world(request):
#     return text("Hello, world.")
#
# app.add_route(uri="/new", handler=hello_world_1, methods=["GET"])


def setup_database():
    @app.listener("after_server_start")
    async def connect_to_db(*args, **kwargs):
        app.ctx.db = create_engine(
            app_config.DB_URL, echo=True if app_config.DEBUG == "True" else False
        )
        await app.ctx.db.connect()

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
