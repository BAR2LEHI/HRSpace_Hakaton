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
