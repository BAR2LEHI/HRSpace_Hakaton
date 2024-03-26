from typing import List

from fastapi import APIRouter, Depends, status
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from .exceptions import NoApplicationExist, NoApplicationsExist
from .schemas import (ApplicationCreateSchema, ApplicationGetSchema,
                      EmploymentStyleCreateSchema, EmploymentStyleGetSchema,
                      SkillCreateSchema, SkillGetSchema,
                      WorkFormatCreateSchema, WorkFormatGetSchema)
from .utils import (create_application, create_employment_style, create_skill,
                    create_work_format, get_app_by_id, get_applications_db)

router_app = APIRouter()


@router_app.get(
    '/',
    response_model=List[ApplicationGetSchema],
    status_code=status.HTTP_200_OK
)
@cache(expire=360)
async def get_applications(
        db: AsyncSession = Depends(get_async_session),
):
    """Роутер получения заявок"""
    all_apps = await get_applications_db(db)
    if not all_apps:
        raise NoApplicationsExist()
    return all_apps


@router_app.get(
    '/{app_id}/',
    response_model=ApplicationGetSchema,
    status_code=status.HTTP_200_OK
)
@cache(expire=360)
async def get_one_application(
        app_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    """Роутер получения заявки по id"""
    app = await get_app_by_id(db, app_id)
    if not app:
        raise NoApplicationExist(app_id)
    return app


@router_app.post(
    '/',
    response_model=ApplicationGetSchema,
    status_code=status.HTTP_201_CREATED
)
async def post_application(
        app: ApplicationCreateSchema,
        db: AsyncSession = Depends(get_async_session)
):
    """Роутер создания заявки"""
    new_app = await create_application(db, app)
    return new_app


@router_app.delete(
    '/{app_id}/'
)
async def delete_application(
        app_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    """Роутер удаления заявки"""
    pass


@router_app.put(
    '/{app_id}/',
    response_model=ApplicationGetSchema,
    status_code=status.HTTP_201_CREATED
)
async def edit_application(
        app_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    """Роутер изменения заявки"""
    pass


@router_app.post(
    '/skills/',
    response_model=SkillGetSchema
)
async def post_skill(
        skill: SkillCreateSchema,
        db: AsyncSession = Depends(get_async_session)
):
    """Роутер добавления скилла"""
    res = await create_skill(db, skill)
    return res


@router_app.post(
    '/work-format/',
    response_model=WorkFormatGetSchema
)
async def post_work_format(
        work_format: WorkFormatCreateSchema,
        db: AsyncSession = Depends(get_async_session)
):
    """Роутер добавления формата работы"""
    res = await create_work_format(db, work_format)
    return res


@router_app.post(
    '/employment-style/',
    response_model=EmploymentStyleGetSchema
)
async def post_employment_style(
        employment_style: EmploymentStyleCreateSchema,
        db: AsyncSession = Depends(get_async_session)
):
    """Роутер добавления ида занятости"""
    res = await create_employment_style(db, employment_style)
    return res
