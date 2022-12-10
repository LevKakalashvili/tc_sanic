from apscheduler.triggers.cron import CronTrigger
from sanic import Sanic

from app.models import User
from app.schedule_task import clear_inactive_user_table
from app.settings import Config as AppConfig
from app.db import db_engine
from app.handlers import UserRegistration, GoodsList, UserActivation, Transaction
from app.urls import Urls as AppUrls
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sanic_jwt import Initialize, exceptions
from passlib.hash import pbkdf2_sha256


async def authenticate(request, *args, **kwargs):

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = User.get(username)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if not pbkdf2_sha256.verify(password, user.password):
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user


# application
app = Sanic("test_sanic_app")
Initialize(app, authenticate=authenticate)
app.ctx.db_engine = db_engine

# routes
app.add_route(UserRegistration.as_view(), AppUrls.USER_REGISTRATION)
app.add_route(UserActivation.as_view(), f"{AppUrls.USER_ACTIVATION}/<activation_link:uuid>")
app.add_route(GoodsList.as_view(), AppUrls.GOODS)
app.add_route(Transaction.as_view(), AppUrls.ADD_TRANSACTION)


# events
@app.after_server_start
async def setup_schedule(app, loop):
    app.ctx.scheduler = AsyncIOScheduler()
    app.ctx.scheduler.add_job(clear_inactive_user_table, CronTrigger.from_crontab(AppConfig.INACTIVE_USER_CLEAR_CRON))
    app.ctx.scheduler.start()


def init():
    User.update_admins(admins=AppConfig.ADMINS_LIST)

    if AppConfig.DEBUG:
        app.run(
            debug=AppConfig.DEBUG,
            host=AppConfig.HOST,
            port=AppConfig.PORT,
            auto_reload=AppConfig.AUTO_RELOAD,
        )
    else:
        app.run()


if __name__ == "__main__":
    init()
