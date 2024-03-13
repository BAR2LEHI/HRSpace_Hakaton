from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from enum import Enum

from ..database import Base


class RolesEnum(str, Enum):
    recruiter = 'recruiter'
    customer = 'customer'
    admin = 'admin'


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    role = Column(pgEnum(RolesEnum), nullable=False)
