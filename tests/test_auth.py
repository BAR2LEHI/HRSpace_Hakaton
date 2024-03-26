from httpx import AsyncClient


async def test_unauthorized_user_logout(ac: AsyncClient):
    response = await ac.post('/auth/jwt/logout')
    assert response.status_code == 401, 'Пользователь залогинен.'


async def test_register(ac: AsyncClient):
    response = await ac.post('/auth/register', json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "first_name": "string",
        "last_name": "string",
        "role": "customer"
    })
    assert response.status_code == 201, "Ошибка регистрации пользователя."


async def test_user_login(ac: AsyncClient):
    await ac.post('/auth/register', json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "first_name": "string",
        "last_name": "string",
        "role": "customer"
    })
    response = await ac.post('/auth/jwt/login', json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "first_name": "string",
        "last_name": "string",
        "role": "customer"
    })
    assert response.status_code == 204, 'Ошибка входа в аккаунт.'


async def test_user_logout(ac: AsyncClient):
    response = await ac.post('/auth/jwt/logout')
    assert response.status_code == 204, 'Ошибка выхода из аккуанта.'
