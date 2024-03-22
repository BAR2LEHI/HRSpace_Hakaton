import asyncio
from typing import List

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Application, EmploymentStyle, Skill, WorkFormat
from .schemas import (ApplicationCreateSchema, EmploymentStyleCreateSchema,
                      SkillCreateSchema, WorkFormatCreateSchema)


async def create_skill(db: AsyncSession,
                       skill_name: str):
    """Создание скилла"""
    new_skill = Skill(
        name=skill_name
    )
    db.add(new_skill)
    return new_skill


async def create_work_format(db: AsyncSession,
                             work_format: WorkFormatCreateSchema):
    """Тех. util для создания формата работы"""
    new_work_format = WorkFormat(
        **work_format.model_dump()
    )
    db.add(new_work_format)
    await db.commit()
    return new_work_format


async def create_employment_style(db: AsyncSession,
                                  employment_style: EmploymentStyleCreateSchema):
    """Тех. util для создания вида занятости"""
    new_emp_style = EmploymentStyle(
        **employment_style.model_dump()
    )
    db.add(new_emp_style)
    await db.commit()
    return new_emp_style


async def get_skills(db: AsyncSession,
                    skill_names: List[SkillCreateSchema]):
    """Получение скиллов по переданному списку их наименований"""
    names = [
        skill['name'] for skill 
        in skill_names
    ]
    stmt = select(
        Skill
    ).where(
        Skill.name.in_(names)
    )
    res = await db.execute(stmt)
    return res.scalars().all()


async def get_work_format(db: AsyncSession,
                          work_format_names: List[WorkFormatCreateSchema]):
    """Получение форматов работы соискателя"""
    wf_names = [wf['title'] for wf in work_format_names]
    stmt = select(
        WorkFormat
    ).where(
        WorkFormat.title.in_(wf_names)
    )
    res = await db.execute(stmt)
    return res.scalars().all()


async def get_employment_style(db: AsyncSession,
                               empl_style_names: List[EmploymentStyleCreateSchema]):
    """Получение видов занятости соискателя"""
    empl_stl_names = [emp['name'] for emp in empl_style_names]
    stmt = select(
        EmploymentStyle
    ).where(
        EmploymentStyle.name.in_(empl_stl_names)
    )
    res = await db.execute(stmt)
    return res.scalars().all()


async def get_or_create_skill(db: AsyncSession,
                              skill_names: List[str]):
    """Получение и создание скиллов"""
    existing_skills = await get_skills(db, skill_names)
    existing_skills_names = [
        skill.name for skill in existing_skills
    ]
    tasks = [
        create_skill(db, skill_name['name'])
        for skill_name in skill_names 
        if skill_name['name'] not in existing_skills_names
    ]
    created_skills = await asyncio.gather(*tasks)
    existing_skills.extend(created_skills)
    return existing_skills


async def get_applications_db(db: AsyncSession):
    stmt = select(Application).options()
    apps = await db.execute(stmt)
    return apps.scalars().unique().all()


async def get_app_by_id(db: AsyncSession,
                        app_id: int):
    stmt = select(
        Application
    ).where(
        Application.id == app_id
    )
    app = await db.execute(stmt)
    return app.scalars().unique().first()


async def create_application(db: AsyncSession,
                             app: ApplicationCreateSchema):
    """Создание новой заявки"""
    app = app.model_dump()
    skills = await get_or_create_skill(db, app.pop('skills'))
    work_format = await get_work_format(db, app.pop('work_format'))
    employment = await get_employment_style(db, app.pop('employment'))
    new_app = Application(**app)
    new_app.work_format.extend(work_format)
    new_app.skills.extend(skills)
    new_app.employment.extend(employment)
    db.add(new_app)
    await db.commit()
    return new_app

