from conftest import ac, async_session_maker
from httpx import AsyncClient
from sqlalchemy import insert, select

from src.Applications.models import Condition, EmploymentStyle, WorkFormat


async def test_add_work_format():
    async with async_session_maker() as session:
        stmt = insert(WorkFormat).values(id=1, title='office')
        await session.execute(stmt)
        await session.commit()

        query = select(WorkFormat).where(WorkFormat.id == 1)
        result = await session.execute(query)
        work_format = result.scalars().all()
        assert ([work_format[0].id, work_format[0].title] == [1, 'office'],
                'Формат работы не был добавлен')


async def test_add_employment_style():
    async with async_session_maker() as session:
        stmt = insert(EmploymentStyle).values(id=1, name='full_time')
        await session.execute(stmt)
        await session.commit()

        query = select(EmploymentStyle).where(EmploymentStyle.id == 1)
        result = await session.execute(query)
        empl_style = result.scalars().all()
        assert ([empl_style[0].id, empl_style[0].name] == [1, 'full_time'],
                'Вид занятости не был добавлен')


async def test_add_condition():
    async with async_session_maker() as session:
        stmt = insert(Condition).values(id=1, name='fitness')
        await session.execute(stmt)
        await session.commit()

        query = select(Condition).where(Condition.id == 1)
        result = await session.execute(query)
        cond = result.scalars().all()
        assert ([cond[0].id, cond[0].name] == [1, 'fitness'])


async def test_post_application(ac: AsyncClient):
    response = await ac.post('/applications/', json={
        "title": "string",
        "status": "draft",
        "company_specialization": "string",
        "address": "string",
        "experience": "without_exp",
        "salary_from": 1,
        "salary_up_to": 2,
        "paperwork": "gph",
        "responsibilities": "string",
        "requirements": "string",
        "payment": 1,
        "workers_number": 1,
        "terms_payment": "all_now",
        "recruiters_number": 1,
        "resume_showing_date": "2024-03-25",
        "desired_release_date": "2024-03-25",
        "recruiter_responsibilities": "string",
        "resume_type": "no_interview",
        "stop_list_employee": "string",
        "skills": [
            {
            "name": "string"
            }
        ],
        "work_format": [
            {
            "title": "office"
            }
        ],
        "employment": [
            {
            "name": "full_time"
            }
        ],
        "conditions": [
            {
            "name": "fitness"
            }
        ]
    })
    assert (response.status_code == 201,
            'Заявка не была создана')


async def test_get_one_application(ac: AsyncClient):
    response = await ac.get('/applications/1/')
    assert (response.status_code == 200,
            'Заявка не существует')


async def test_get_applications(ac: AsyncClient):
    response = await ac.post('/applications/', json={
        "title": "string",
        "status": "draft",
        "company_specialization": "string",
        "address": "string",
        "experience": "without_exp",
        "salary_from": 1,
        "salary_up_to": 2,
        "paperwork": "gph",
        "responsibilities": "string",
        "requirements": "string",
        "payment": 1,
        "workers_number": 1,
        "terms_payment": "all_now",
        "recruiters_number": 1,
        "resume_showing_date": "2024-03-25",
        "desired_release_date": "2024-03-25",
        "recruiter_responsibilities": "string",
        "resume_type": "no_interview",
        "stop_list_employee": "string",
        "skills": [
            {
            "name": "string"
            }
        ],
        "work_format": [
            {
            "title": "office"
            }
        ],
        "employment": [
            {
            "name": "full_time"
            }
        ],
        "conditions": [
            {
            "name": "fitness"
            }
        ]
    })
    assert (response.status_code == 201,
            'Заявка не была создана')
    response_get = await ac.get('/applications/')
    assert (response_get.status_code == 200,
            'Заявок нет')
    assert (len(response_get.json()) == 2,
            'Кол-во заявок не равняется 2')


async def test_delete_application(ac: AsyncClient):
    response = await ac.delete('/applications/1/')
    assert (response.status_code == 200, 
            'Заявка не была удалена')
    response_2 = await ac.delete('/applications/2/')
    assert (response_2.status_code == 200, 
            'Заявка не была удалена')
