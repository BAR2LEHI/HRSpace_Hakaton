from enum import Enum

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM as pgEnum

from ..database import Base


class RolesEnum(str, Enum):
    recruiter = 'recruiter'
    customer = 'customer'
    admin = 'admin'


class User(SQLAlchemyBaseUserTable[int], Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hashed_password = Column(
        String(length=1024), nullable=False
    )
    email = Column(String, nullable=False, unique=True)
    role = Column(pgEnum(RolesEnum), default='customer', nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(
        Boolean, default=False, nullable=False
    )
    is_verified = Column(
        Boolean, default=False, nullable=False
    )
