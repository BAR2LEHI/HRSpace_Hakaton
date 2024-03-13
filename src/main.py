from fastapi import FastAPI
from .Applications.router import router_app
from .Users.router import router_user


app = FastAPI(
    title='HRSpace',
    version='0.0.1',
    license_info={
        'name': 'HRSpace',
        'url': 'https://hrspace.hh.ru/',
    }
)


app.include_router(router_app)
app.include_router(router_user)
