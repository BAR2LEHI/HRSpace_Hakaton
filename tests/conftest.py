import asyncio
import pytest

from typing import AsyncGenerator
from httpx import AsyncClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


from src.config import (
    DB_HOST_TEST, DB_NAME_TEST, DB_PORT_TEST,
    DB_PASS_TEST, DB_USER_TEST
)
from src.main import app
from src.database import get_async_session, Base


TEST_DATABASE_URL = (
    f'postgresql+asyncpg:/'
    f'/{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:'
    f'{DB_PORT_TEST}/{DB_NAME_TEST}'
)

# Создаём асинхронный движок на основе которого
# будут создаваться сессии для работы с БД
engine_test = create_async_engine(TEST_DATABASE_URL, poolclass=NullPool)

# Класс sessionmaker'а, который будет отдавать
# нам асинхронную сессию для подключения к БД
async_session = sessionmaker(engine_test, class_=AsyncSession,
                             expire_on_commit=False)
metadata = Base.metadata
metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac
