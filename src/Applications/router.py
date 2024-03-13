from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from . import schemas
from typing import List


router_app = APIRouter(
    prefix='/applications',
    tags=['Applications',]
)


@router_app.get('/', response_model=List[schemas.Application])
async def get_applications(
    db: AsyncSession = Depends(get_async_session),
):
    pass


@router_app.post('/', response_model=schemas.Application)
async def create_application(
    app: schemas.Application,
    db: AsyncSession = Depends(get_async_session)
):
    pass

