from sanic import Blueprint, text

user = Blueprint(
    "user",
    __name__,
)


@user.route("/login")
async def index(request):
    return text("Login route form")
