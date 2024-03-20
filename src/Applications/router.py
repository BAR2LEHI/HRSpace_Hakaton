from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from .schemas import (ApplicationCreateSchema, ApplicationGetSchema,
                      EmploymentStyleCreateSchema, EmploymentStyleGetSchema,
                      SkillCreateSchema, SkillGetSchema,
                      WorkFormatCreateSchema, WorkFormatGetSchema)
from .utils import (create_application, create_employment_style, create_skill,
                    create_work_format)

router_app = APIRouter(
    prefix='/applications',
    tags=['Applications',]
)


@router_app.get(
    '/', 
    response_model=List[ApplicationGetSchema], 
    status_code=status.HTTP_200_OK
)
async def get_applications(
    db: AsyncSession = Depends(get_async_session),
):
    pass


@router_app.get(
    '/{app_id}/', 
    response_model=ApplicationGetSchema, 
    status_code=status.HTTP_200_OK
)
async def get_one_application(
    app_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    pass


@router_app.post(
    '/', 
    response_model=ApplicationGetSchema, 
    status_code=status.HTTP_201_CREATED
)
async def post_application(
    app: ApplicationCreateSchema,
    db: AsyncSession = Depends(get_async_session)
):
    new_app = await create_application(db, app)
    return new_app


@router_app.put(
    '/{app_id}/', 
    response_model=ApplicationGetSchema, 
    status_code=status.HTTP_201_CREATED
)
async def edit_application(
    app_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    pass


@router_app.post(
    '/skills/',
    response_model=SkillGetSchema
)
async def post_skill(
    skill: SkillCreateSchema,
    db: AsyncSession = Depends(get_async_session)
):
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
    res = await create_work_format(db, work_format)
    return res


@router_app.post(
    '/employment-style/',
    response_model=EmploymentStyleGetSchema
)
async def post_work_format(
    employment_style: EmploymentStyleCreateSchema,
    db: AsyncSession = Depends(get_async_session)
):
    res = await create_employment_style(db, employment_style)
    return res
