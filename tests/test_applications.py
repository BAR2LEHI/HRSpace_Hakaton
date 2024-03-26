from sqlalchemy import insert, select

from src.Applications.models import WorkFormat, EmploymentStyle
from conftest import client, async_session_maker


async def test_add_work_format():
    async with async_session_maker() as session:
        stmt = insert(WorkFormat).values(id=1, title='office')
        await session.execute(stmt)
        await session.commit()

        query = select(WorkFormat)
        result = await session.execute(query)
        work_format = result.scalars().all()
        assert [work_format[0].id, work_format[0].title] == [1, 'office'], 'Формат работы не был добавлен'


async def test_add_employment_style():
    async with async_session_maker() as session:
        stmt = insert(EmploymentStyle).values(id=1, title='full_time')
        await session.execute(stmt)