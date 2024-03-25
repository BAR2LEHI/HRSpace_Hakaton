import json
from typing import List, Dict

from fastapi.responses import JSONResponse
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from .redis import redis
from .utils import load_data_to_redis


directory_router = APIRouter()


@directory_router.get(
    '/skills/', 
    response_model=Dict
)
@cache(expire=360)
async def get_directory_skills():
    skills_names = await redis.get('skills')
    return {'skills': json.loads(skills_names)}


@directory_router.get(
    '/job-titles/', 
    response_model=Dict
)
@cache(expire=360)
async def get_directory_job_title():
    job_titles = await redis.get('job_titles')
    return {'job_titles': json.loads(job_titles)}


@directory_router.get(
    '/specializations/', 
    response_model=Dict
)
@cache(expire=360)
async def get_directory_specialization():
    specs = await redis.get('specialization')
    return {'specializations': json.loads(specs)}


@directory_router.post(
    '/load_data/'
)
async def load_data():
    await load_data_to_redis()
    return {'detail': 'Данные успешно загружены'}
