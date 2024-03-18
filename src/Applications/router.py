from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from .schemas import ApplicationSchema, SkillSchema
from typing import List
from .utils import create_application, create_skill


router_app = APIRouter(
    prefix='/applications',
    tags=['Applications',]
)


@router_app.get(
    '/', 
    response_model=List[ApplicationSchema], 
    status_code=status.HTTP_200_OK
)
async def get_applications(
    db: AsyncSession = Depends(get_async_session),
):
    pass


@router_app.get(
    '/{app_id}/', 
    response_model=ApplicationSchema, 
    status_code=status.HTTP_200_OK
)
async def get_one_application(
    app_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    pass


@router_app.post(
    '/', 
    response_model=ApplicationSchema, 
    status_code=status.HTTP_201_CREATED
)
async def post_application(
    app: ApplicationSchema,
    db: AsyncSession = Depends(get_async_session)
):
    new_app = await create_application(db, app)
    return new_app


@router_app.put(
    '/{app_id}/', 
    response_model=ApplicationSchema, 
    status_code=status.HTTP_201_CREATED
)
async def edit_application(
    app_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    pass


@router_app.post(
    '/skills/',
    response_model=SkillSchema
)
async def post_skill(
    skill: SkillSchema,
    db: AsyncSession = Depends(get_async_session)
):
    res = await create_skill(db, skill)
    return res