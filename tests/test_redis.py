from conftest import ac
from data_for_test import (job_titles_example, skills_example,
                           specializations_example)
from httpx import AsyncClient


async def test_get_directory_skills(ac: AsyncClient):
    response = await ac.get('/directories/skills/')
    assert (response.json() == skills_example, 
            'Нет подключения к Redis или отсутствует ключ = "skills"')


async def test_get_directory_job_title(ac: AsyncClient):
    response = await ac.get('/directories/job-titles/')
    assert (response.json() == job_titles_example, 
            'Нет подключения к Redis или отсутствует ключ = "job_titles"')


async def test_directory_specialization(ac: AsyncClient):
    response = await ac.get('/directories/specializations/')
    assert (response.json() == specializations_example, 
            'Нет подключения к Redis или отсутствует ключ = "specializations"')
