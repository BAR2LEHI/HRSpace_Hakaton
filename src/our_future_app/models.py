from sqlalchemy import Integer, Column, String

from ..database import Base


class TestTable(Base):

    __tablename__ = 'test_table'

    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String,
        unique=True
    )
    num = Column(
        Integer
    )
