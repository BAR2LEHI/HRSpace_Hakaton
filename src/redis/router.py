import json
from typing import List

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from ..Applications.exceptions import NoConnectionWithRedis
from .redis import redis
from .utils import load_data_to_redis

directory_router = APIRouter()


@directory_router.get(
    '/skills/',
    response_model=List[str]
)
@cache(expire=360)
async def get_directory_skills():
    """Роутер получения скиллов"""
    try:
        skills_names = await redis.get('skills')
    except:
        raise NoConnectionWithRedis(
            name='Нет соединения с Redis'
        )
    return json.loads(skills_names)


@directory_router.get(
    '/job-titles/',
    response_model=List[str]
)
@cache(expire=360)
async def get_directory_job_title():
    """Роутер получения названий работы"""
    try:
        job_titles = await redis.get('job_titles')
    except:
        raise NoConnectionWithRedis(
            name='Нет соединения с Redis'
        )
    return json.loads(job_titles)


@directory_router.get(
    '/specializations/',
    response_model=List[str]
)
@cache(expire=360)
async def get_directory_specialization():
    """Роутер получения специализации"""
    try:
        specs = await redis.get('specialization')
    except:
        raise NoConnectionWithRedis(
            name='Нет соединения с Redis'
        )
    return json.loads(specs)


@directory_router.post(
    '/load_data/'
)
async def load_data():
    """Роутер загрузки данных"""
    await load_data_to_redis()
    return {'detail': 'Данные успешно загружены'}
