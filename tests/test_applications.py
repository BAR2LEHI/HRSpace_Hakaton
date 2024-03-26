from sqlalchemy import insert, select

from src.Applications.models import WorkFormat
from conftest import client, async_session_maker


async def test_add_work_format():
    async with async_session_maker() as session:
        print(session)
        wf = WorkFormat(id=1, title='office')
        await session.add(wf)
        await session.commit()

        query = select(WorkFormat)
        result = await session.execute(query)
        assert result.all() == [(1, 'office')], 'Формат работы не был добавлен'
