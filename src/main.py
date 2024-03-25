from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from .redis.router import directory_router
from .Applications.router import router_app
from .redis.redis import redis
from .Users.router import router_user, router_user_register


@asynccontextmanager
async def lifespan(app: FastAPI):
    FastAPICache.init(
        RedisBackend(redis),
        prefix='fastapi-cache'
    )
    yield


app = FastAPI(
    root_path="/api",
    lifespan=lifespan,
    title='HRSpace',
    version='0.0.1',
    license_info={
        'name': 'HRSpace',
        'url': 'https://hrspace.hh.ru/',
    }
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
