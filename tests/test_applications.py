from sqlalchemy import insert, select

from src.Applications.models import WorkFormat
from conftest import client, async_session_maker


async def test_add_work_format():
    async with async_session_maker() as session:
        stmt = insert(WorkFormat).values(id=1, title='office')
        await session.execute(stmt)
        await session.commit()

        query = select(WorkFormat)
        result = await session.execute(query)
        work_format = result.scalars().all()
        assert result.scalars().all() == [(1, 'office')], 'Формат работы не был добавлен'
