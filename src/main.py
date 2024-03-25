from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from .redis.router import directory_router
from .Applications.router import router_app
from .redis.redis import redis
from .Users.router import router_user, router_user_register
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    FastAPICache.init(
        RedisBackend(redis), 
        prefix='fastapi-cache'
    )
    yield


origins = [
    'http://frontend_app',
    'http://localhost:3002',
    'http://hrspace.sytes.net:3002',
    'https://localhost:3002',
    'http://localhost:3002'
]


app = FastAPI(
    lifespan=lifespan,
    title='HRSpace',
    version='0.0.1',
    license_info={
        'name': 'HRSpace',
        'url': 'https://hrspace.hh.ru/',
    }
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    router_app,
    prefix='/applications',
    tags=['Applications',]
)
app.include_router(
    router_user,
    prefix='/auth/jwt',
    tags=['auth']
)
app.include_router(
    router_user_register,
    prefix='/auth',
    tags=['auth']
)
app.include_router(
    directory_router,
    prefix='/directories',
    tags=['directories']
)