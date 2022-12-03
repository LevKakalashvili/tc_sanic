from dataclasses import dataclass


@dataclass
class Urls:
    USER = "/user"
    USER_LOGIN = "/user/login"
    USER_REGISTRATION = "/user/registration"
    USER_ACTIVATION = "/user/activation"
    GOODS = "/good/all"
