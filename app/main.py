from sanic import Sanic
from app.settings import AppSetting

app = Sanic(__name__)

def setup_database():
    app.ctx.db = ...

    # @app.listener('after_server_start')
    # async def connect_to_db(*args, **kwargs):
    #     await app.db.connect()
    #
    # @app.listener('after_server_stop')
    # async def disconnect_from_db(*args, **kwargs):
    #     await app.db.disconnect()

def init():

    app.config.update_config(AppSetting)

    app.run()
