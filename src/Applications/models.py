from sqlalchemy import Integer, Column, String
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from ..database import Base
from enum import Enum


class StatusEnum(str, Enum):
    approved = 'approved'
    moderation = 'moderation'
    accept = 'accept'
    close = 'close'


class Application(Base):
    """Модель заявки"""

    __tablename__ = 'application'

    id = Column(Integer, primary_key=True, unique=True)
    status = Column(pgEnum(StatusEnum), nullable=True)
    
