from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


class AdminAuth(AuthenticationBackend):
    """Модель аутентификации админ-зоны"""
    async def login(self, request: Request) -> bool:
        await request.form()

        request.session.update({"token": "..."})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        return True


authentication_backend = AdminAuth(secret_key="SECRET")
