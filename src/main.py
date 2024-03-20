from fastapi import FastAPI
from .Applications.router import router_app
from .Users.router import router_user, router_user_register

app = FastAPI(
    title='HRSpace',
    version='0.0.1',
    license_info={
        'name': 'HRSpace',
        'url': 'https://hrspace.hh.ru/',
    }
)

app.include_router(router_app)
app.include_router(
    router_user,
    prefix="/auth/jwt",
    tags=["auth"]
)
app.include_router(
    router_user_register,
    prefix="/auth",
    tags=["auth"]
)
