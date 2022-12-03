from sanic import request as request_type


def check_credentials(request: request_type) -> bool:
    if getattr(request, "credentials") is not None \
            and (request.credentials.username and request.credentials.password):
        return True
    return False
