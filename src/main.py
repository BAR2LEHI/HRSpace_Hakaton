from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.middleware.cors import CORSMiddleware

from sqladmin import Admin

from .redis.router import directory_router
from .Applications.router import router_app
from .redis.redis import redis
from .Users.router import router_user, router_user_register
from .Admin.auth import authentication_backend

from .database import engine
from .Admin.models import (
    UserAdmin, SkillAdmin, ConditionAdmin,
    WorkFormatAdmin, EmploymentStyleAdmin,
    AppSkillAdmin, AppFormatAdmin, AppConditionAdmin,
    AppEmploymentAdmin, ApplicationAdmin
)


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

admin = Admin(app, engine=engine, authentication_backend=authentication_backend)

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
