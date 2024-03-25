from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from sqladmin import Admin

from .Admin.auth import authentication_backend
from .Admin.models import (AppConditionAdmin, AppEmploymentAdmin,
                           AppFormatAdmin, ApplicationAdmin, AppSkillAdmin,
                           ConditionAdmin, EmploymentStyleAdmin, SkillAdmin,
                           UserAdmin, WorkFormatAdmin)
from .Applications.exceptions import NoApplicationExist, NoConnectionWithRedis
from .Applications.router import router_app
from .database import engine
from .redis.redis import redis
from .redis.router import directory_router
from .Users.router import router_user, router_user_register


@asynccontextmanager
async def lifespan(app: FastAPI):
    FastAPICache.init(
        RedisBackend(redis),
        prefix='fastapi-cache'
    )
    yield


origins = [
    'http://hrspace.sytes.net:3002',
    'https://hrspace.sytes.net:3002',
    'http://localhost:3002',
    'https://localhost:3002',
    'http://frontend_app',
]


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


admin = Admin(app, engine=engine, authentication_backend=authentication_backend)


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


@app.exception_handler(NoApplicationExist)
async def app_does_not_exist_handler(
    request: Request,
    exc: NoApplicationExist
):
    return JSONResponse(
        status_code=404,
        content={
            'detail': exc.name
        }
    )


@app.exception_handler(NoConnectionWithRedis)
async def no_connect_with_redis_handler(
    request: Request,
    exc: NoConnectionWithRedis
):
    return JSONResponse(
        status_code=503,
        content={
            'detail': exc.name
        }
    )


admin.add_view(UserAdmin)
admin.add_view(SkillAdmin)
admin.add_view(AppSkillAdmin)
admin.add_view(ConditionAdmin)
admin.add_view(WorkFormatAdmin)
admin.add_view(EmploymentStyleAdmin)
admin.add_view(AppFormatAdmin)
admin.add_view(AppConditionAdmin)
admin.add_view(AppEmploymentAdmin)
admin.add_view(ApplicationAdmin)
