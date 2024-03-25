from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from sqladmin import Admin
from fastapi.responses import JSONResponse
from .redis.router import directory_router
from .Applications.router import router_app
from .redis.redis import redis
from .Users.router import router_user, router_user_register
from fastapi.middleware.cors import CORSMiddleware
from .Admin.auth import authentication_backend

from .Applications.exceptions import NoApplicationExist, NoApplicationsExist
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
async def no_application_handler(request: Request, exc: NoApplicationExist):
    return JSONResponse(
        status_code=404,
        content={
            'detail':f'Заявки с id={exc.id} не существует.' 
        }
    )


@app.exception_handler(NoApplicationsExist)
async def no_applications_handler(request: Request, exc: NoApplicationsExist):
    return JSONResponse(
        status_code=404,
        content={
            'detail':'В базе данных ещё нет заявок.' 
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
