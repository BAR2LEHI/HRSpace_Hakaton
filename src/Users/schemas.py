from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Схема для получения пользователя"""
    id: int
    first_name: str
    last_name: str
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    role: Optional[str] = 'customer'

    class ConfigDict:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания пользователя"""
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    role: Optional[str] = 'customer'

    class ConfigDict:
        exclude = {"role"}
