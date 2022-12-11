from pydantic import ValidationError
from sanic_jwt import exceptions
from passlib.hash import pbkdf2_sha256
from app.models import User
from app.validators import UserData


async def authenticate(request, *args, **kwargs):
    try:
        user_data = UserData(**request.json)

        user = User.get(user_data.username)
        if user is None:
            raise exceptions.AuthenticationFailed("User not found.")

        if not pbkdf2_sha256.verify(user_data.password, user.password):
            raise exceptions.AuthenticationFailed("Password is incorrect.")

    except ValidationError:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    return user
