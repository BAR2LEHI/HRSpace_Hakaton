import json
from typing import List

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.redis import redis

directory_router = APIRouter()


@directory_router.get(
    '/skills/', 
    response_model=List[str]
)
@cache(expire=360)
async def get_directory_skills():
    skills_names = await redis.get('skills')
    return json.loads(skills_names)


@directory_router.get(
    '/job-titles/', 
    response_model=List[str]
)
@cache(expire=360)
async def get_directory_job_title():
    job_titles = await redis.get('job_titles')
    return json.loads(job_titles)


@directory_router.get(
    '/specializations/', 
    response_model=List[str]
)
@cache(expire=360)
async def get_directory_specialization():
    specs = await redis.get('specs')
    return json.loads(specs)