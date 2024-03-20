from fastapi_users import FastAPIUsers

from .auth import auth_backend
from .manager import get_user_manager
from .schemas import UserRead, UserCreate
from .models import User


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router_user = fastapi_users.get_auth_router(auth_backend)

router_user_register = fastapi_users.get_register_router(UserRead, UserCreate)
