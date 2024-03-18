from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String, Boolean, Table, MetaData
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from enum import Enum


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


metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True, unique=True),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column(
        'hashed_password', String(length=1024), nullable=False
    ),
    Column('email', String, nullable=False, unique=True),
    Column('role', pgEnum(RolesEnum), default='customer', nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column(
        'is_superuser', Boolean, default=False, nullable=False
    ),
    Column(
        'is_verified', Boolean, default=False, nullable=False
    ),
)
