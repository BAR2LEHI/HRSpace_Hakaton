from sqlalchemy import (CheckConstraint, Column, DateTime, ForeignKey, Integer,
                        String)
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.orm import relationship

from ..database import Base
from .enums import (EmploymentEnum, ExperienceEnum, PaperWorkEnum, StatusEnum,
                    TermsPaymentEnum, TermsRecruiterEnum, TypesResumeEnum, FormatEnum)


class AppSkill(Base):
    """Таблица ассоциации скилла и заявки"""

    __tablename__ = 'skill_to_application'

    application_id = Column(Integer, ForeignKey('application.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)


class AppFormat(Base):
    """Таблица ассоциации формата и заявки"""

    __tablename__ = 'format_to_application'

    application_id = Column(Integer, ForeignKey('application.id'), primary_key=True)
    format_id = Column(Integer, ForeignKey('work_format.id'), primary_key=True)


class AppEmployment(Base):
    """Таблица ассоциации занятости и заявки"""

    __tablename__ = 'employment_to_application'

    application_id = Column(Integer, ForeignKey('application.id'), primary_key=True)
    employment_id = Column(Integer, ForeignKey('employment.id'), primary_key=True)


class Application(Base):
    """Модель заявки"""

    __tablename__ = 'application'

    id = Column(
        Integer, 
        primary_key=True, 
        unique=True
    )
    title = Column(
        String, 
        nullable=False
    )
    status = Column(
        pgEnum(StatusEnum), 
        nullable=True
    )
    skills = relationship(
        'Skill', 
        secondary='skill_to_application'
    )
    company_specialization = Column(
        String, 
        nullable=False
    )
    work_format = relationship(
        'WorkFormat', 
        secondary='format_to_application'
    )
    address = Column(
        String, 
        nullable=True
    )
    experience = Column(
        pgEnum(ExperienceEnum), 
        nullable=False
    )
    employment = relationship(
        'EmploymentStyle', 
        secondary='employment_to_application'
    )
    salary_from = Column(
        Integer, 
        nullable=True
    )
    salary_up_to = Column(
        Integer, 
        nullable=True
    )
    paperwork = Column(
        pgEnum(PaperWorkEnum), 
        nullable=False
    )
    responsibilities = Column(
        String, 
        nullable=True
    )
    requirements = Column(
        String, 
        nullable=True
    )
    conditions = Column(
        String, 
        nullable=True
    )
    payment = Column(
        Integer, 
        nullable=False
    )
    terms_payment = Column(
        pgEnum(TermsPaymentEnum), 
        nullable=False
    )
    recruiters_number = Column(
        Integer, 
        nullable=False
    )
    resume_showing_date = Column(
        DateTime,
        nullable=False
    )
    desired_release_date = Column(
        DateTime,
        nullable=False
    )
    recruiter_responsibilities = Column(
        String, 
        nullable=True
    )
    resume_type = Column(
        pgEnum(TypesResumeEnum),
        nullable=True
    )
    terms_recruiter = Column(
        pgEnum(TermsRecruiterEnum),
        nullable=False
    )
    comments = Column(
        String,
        nullable=True
    )
    stop_list_employee = Column(
        String,
        nullable=True
    )


    __table_args__ = (
        CheckConstraint(
            'recruiters_number >= 1 AND recruiters_number <= 3',
            name='Лимит нанимаемых рекрутеров'
        ),
        CheckConstraint(
            'payment > 0',
            name='Мин. оплата труда рекрутера'
        ),
        CheckConstraint(
            'salary_from <= salary_up_to',
            name='Максимальная планка зп не может быть меньше минимальной'
        )
    )


class Skill(Base):
    """Модель профессионального навыка"""

    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False)


class WorkFormat(Base):
    """Модель формата работы"""

    __tablename__ = 'work_format'

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(pgEnum(FormatEnum), nullable=False, unique=True)


class EmploymentStyle(Base):
    """Модель занятости"""

    __tablename__ = 'employment'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(pgEnum(EmploymentEnum), nullable=True, unique=True)
