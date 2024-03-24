from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# Ссылка на базу данных PostgreSQL
SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Создаём асинхронный движок на основе которого будут создаваться сессии для работы с БД
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

# Класс sessionmaker'а, который будет отдавать нам асинхронную сессию для подключения к БД
async_local_session = sessionmaker(engine, class_=AsyncSession,
                                   expire_on_commit=False)

# Базовый класс SQLAlchemy для последующего создания моделей
Base = declarative_base()


# Асинхронный генератор, который при вызове отдаёт готовую асинх сессию
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_local_session() as session:
        yield session
