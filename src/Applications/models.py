<<<<<<< HEAD
from sqlalchemy import (CheckConstraint, Column, DateTime, ForeignKey, Integer,
                        String)
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.orm import relationship

from ..database import Base
from .enums import (EmploymentEnum, ExperienceEnum, FormatEnum, PaperWorkEnum,
                    StatusEnum, TermsPaymentEnum,
                    TypesResumeEnum, ConditionsEnum)


class AppSkill(Base):
    """Таблица ассоциации скилла и заявки"""

    __tablename__ = 'skill_to_application'

    application_id = Column(
        Integer,
        ForeignKey('application.id'),
        primary_key=True
    )
    skill_id = Column(
        Integer,
        ForeignKey('skill.id'),
        primary_key=True
    )


class AppFormat(Base):
    """Таблица ассоциации формата и заявки"""

    __tablename__ = 'format_to_application'

    application_id = Column(
        Integer,
        ForeignKey('application.id'),
        primary_key=True
    )
    format_id = Column(
        Integer,
        ForeignKey('work_format.id'),
        primary_key=True
    )


class AppEmployment(Base):
    """Таблица ассоциации занятости и заявки"""

    __tablename__ = 'employment_to_application'

    application_id = Column(
        Integer,
        ForeignKey('application.id'),
        primary_key=True
    )
    employment_id = Column(
        Integer,
        ForeignKey('employment.id'),
        primary_key=True
    )


class AppCondition(Base):
    """Таблица ассоциации условия для соискателя и заявки"""

    __tablename__ = 'condition_to_application'

    condition_id = Column(
        Integer,
        ForeignKey('condition.id'),
        primary_key=True
    )
    application_id = Column(
        Integer,
        ForeignKey('application.id'),
        primary_key=True
    )


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
        secondary='skill_to_application',
        lazy='subquery'
    )
    company_specialization = Column(
        String,
        nullable=True
    )
    work_format = relationship(
        'WorkFormat',
        secondary='format_to_application',
        lazy='subquery'
    )
    address = Column(
        String,
        nullable=True
    )
    experience = Column(
        pgEnum(ExperienceEnum),
        nullable=True
    )
    employment = relationship(
        'EmploymentStyle',
        secondary='employment_to_application',
        lazy='subquery'
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
        nullable=True
    )
    responsibilities_requirements = Column(
        String,
        nullable=True
    )
    conditions = relationship(
        'Condition',
        secondary='condition_to_application',
        lazy='subquery'
    )
    payment = Column(
        Integer,
        nullable=False
    )
    workers_number = Column(
        Integer,
        nullable=False
    )
    terms_payment = Column(
        pgEnum(TermsPaymentEnum),
        nullable=False
    )
    recruiters_number = Column(
        Integer,
        nullable=True
    )
    resume_showing_date = Column(
        DateTime,
        nullable=True,
    )
    desired_release_date = Column(
        DateTime,
        nullable=True
    )
    recruiter_responsibilities = Column(
        String,
        nullable=True
    )
    resume_type = Column(
        pgEnum(TypesResumeEnum),
        nullable=True
    )
    recruiter_responsibilities = Column(
        String,
        nullable=True
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


class Condition(Base):
    """Модель условия для соискателя"""

    __tablename__ = 'condition'

    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    name = Column(
        pgEnum(ConditionsEnum),
        unique=True,
        nullable=False
    )


class Skill(Base):
    """Модель профессионального навыка"""

    __tablename__ = 'skill'

    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    name = Column(
        String,
        unique=True,
        nullable=False
    )


class WorkFormat(Base):
    """Модель формата работы"""

    __tablename__ = 'work_format'

    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    title = Column(
        pgEnum(FormatEnum),
        nullable=False,
        unique=True
    )


class EmploymentStyle(Base):
    """Модель занятости"""

    __tablename__ = 'employment'

    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    name = Column(
        pgEnum(EmploymentEnum),
        nullable=True,
        unique=True
    )
=======
from sqlalchemy import (CheckConstraint, Column, DateTime, ForeignKey, Integer,
                        String)
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.orm import relationship

from ..database import Base
from .enums import (EmploymentEnum, ExperienceEnum, FormatEnum, PaperWorkEnum,
                    StatusEnum, TermsPaymentEnum,
                    TypesResumeEnum, ConditionsEnum)


class AppSkill(Base):
    """Таблица ассоциации скилла и заявки"""

    __tablename__ = 'skill_to_application'

    application_id = Column(
        Integer, 
        ForeignKey('application.id'), 
        primary_key=True
    )
    skill_id = Column(
        Integer, 
        ForeignKey('skill.id'), 
        primary_key=True
    )


class AppFormat(Base):
    """Таблица ассоциации формата и заявки"""

    __tablename__ = 'format_to_application'

    application_id = Column(
        Integer, 
        ForeignKey('application.id'), 
        primary_key=True
    )
    format_id = Column(
        Integer, 
        ForeignKey('work_format.id'), 
        primary_key=True
    )


class AppEmployment(Base):
    """Таблица ассоциации занятости и заявки"""

    __tablename__ = 'employment_to_application'

    application_id = Column(
        Integer, 
        ForeignKey('application.id'), 
        primary_key=True
    )
    employment_id = Column(
        Integer, 
        ForeignKey('employment.id'), 
        primary_key=True
    )


class AppCondition(Base):
    """Таблица ассоциации условия для соискателя и заявки"""

    __tablename__ = 'condition_to_application'

    condition_id = Column(
        Integer,
        ForeignKey('condition.id'),
        primary_key=True
    )
    application_id = Column(
        Integer, 
        ForeignKey('application.id'), 
        primary_key=True
    )


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
        secondary='skill_to_application',
        lazy='subquery'
    )
    company_specialization = Column(
        String,
        nullable=True
    )
    work_format = relationship(
        'WorkFormat',
        secondary='format_to_application',
        lazy='subquery'
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
        secondary='employment_to_application',
        lazy='subquery'
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
        nullable=True
    )
    responsibilities_requirements = Column(
        String,
        nullable=True
    )
    conditions = relationship(
        'Condition',
        secondary='condition_to_application',
        lazy='subquery'
    )
    payment = Column(
        Integer,
        nullable=False
    )
    workers_number = Column(
        Integer,
        nullable=False
    )
    terms_payment = Column(
        pgEnum(TermsPaymentEnum),
        nullable=False
    )
    recruiters_number = Column(
        Integer,
        nullable=True
    )
    resume_showing_date = Column(
        DateTime,
        nullable=True,
    )
    desired_release_date = Column(
        DateTime,
        nullable=True
    )
    recruiter_responsibilities = Column(
        String,
        nullable=True
    )
    resume_type = Column(
        pgEnum(TypesResumeEnum),
        nullable=True
    )
    recruiter_responsibilities = Column(
        String,
        nullable=True
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


class Condition(Base):
    """Модель условия для соискателя"""

    __tablename__ = 'condition'

    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    name = Column(
        pgEnum(ConditionsEnum),
        unique=True, 
        nullable=False
    )

    def __str__(self):
        return self.name.name


class Skill(Base):
    """Модель профессионального навыка"""

    __tablename__ = 'skill'

    id = Column(
        Integer, 
        primary_key=True, 
        unique=True
    )
    name = Column(
        String, 
        unique=True, 
        nullable=False
    )

    def __str__(self):
        return self.name


class WorkFormat(Base):
    """Модель формата работы"""

    __tablename__ = 'work_format'

    id = Column(
        Integer, 
        primary_key=True, 
        unique=True
    )
    title = Column(
        pgEnum(FormatEnum), 
        nullable=False, 
        unique=True
    )

    def __str__(self):
        return self.title.name


class EmploymentStyle(Base):
    """Модель занятости"""

    __tablename__ = 'employment'

    id = Column(
        Integer, 
        primary_key=True, 
        unique=True
    )
    name = Column(
        pgEnum(EmploymentEnum), 
        nullable=True, 
        unique=True
    )

    def __str__(self):
        return self.name
>>>>>>> dcbd0231447a19e42e108c0744af24682a7509d7
