from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ApplicationSchema, SkillSchema
from .models import Application, Skill


async def create_application(db: AsyncSession,
                             app: ApplicationSchema):
    """Создание новой заявки"""
    print(app.model_dump())
    new_app = Application(**app.dict())
    db.add(new_app)
    await db.commit()
    return 


async def create_skill(db: AsyncSession,
                       skill: SkillSchema):
    new_skill = Skill(**skill)
    db.add(new_skill)
    await db.commit()
    return new_skill
