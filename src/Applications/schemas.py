from datetime import datetime
from typing import Annotated, List, Optional

from pydantic import BaseModel, conint, model_validator

from .enums import (EmploymentEnum, ExperienceEnum, FormatEnum, PaperWorkEnum,
                    TermsPaymentEnum, TypesResumeEnum, ConditionsEnum)


class SkillCreateSchema(BaseModel):
    """Схема для создания навыка"""
    name: str


class SkillGetSchema(SkillCreateSchema):
    """Схема для получения навыка"""
    id: int


class WorkFormatCreateSchema(BaseModel):
    """Схема создания формата работы"""
    title: FormatEnum


class WorkFormatGetSchema(WorkFormatCreateSchema):
    """Схема для получения формата работы"""
    id: int


class EmploymentStyleCreateSchema(BaseModel):
    """Схема создания типа занятости соискателя"""
    name: EmploymentEnum


class EmploymentStyleGetSchema(EmploymentStyleCreateSchema):
    """Схема получения типа занятости соискателя"""
    id: int


class ConditionCreateSchema(BaseModel):
    """Схема создания условия для соискателя"""
    name: ConditionsEnum


class ConditionGetSchema(ConditionCreateSchema):
    """Схема полученя условия для соискателя"""
    id: int


class ApplicationBaseSchema(BaseModel):
    """Базовая схема заявки"""
    title: str
    company_specialization: str
    address: Optional[str] = None
    experience: ExperienceEnum
    salary_from: Optional[int] = None
    salary_up_to: Optional[int] = None
    paperwork: PaperWorkEnum
    responsibilities_requirements: Optional[str] = None
    payment: Annotated[int, conint(ge=1)]
    workers_number: int
    terms_payment: TermsPaymentEnum
    recruiters_number: Annotated[int, conint(ge=1, le=3)]
    resume_showing_date: datetime
    desired_release_date: datetime
    recruiter_responsibilities: Optional[str] = None
    resume_type: TypesResumeEnum
    stop_list_employee: Optional[str] = None

    @model_validator(mode='after')
    def check_salary_up(self):
        if self.salary_from > self.salary_up_to:
            raise ValueError('Максимальная планка зарплаты не может быть больше минимальной')
        return self


class ApplicationGetSchema(ApplicationBaseSchema):
    """Схема отображения заявки"""
    id: int
    skills: Optional[List[SkillGetSchema]] = None
    work_format: List[WorkFormatGetSchema]
    employment: List[EmploymentStyleGetSchema]
    conditions: List[ConditionGetSchema]

    class config:
        orm_mode = True


class ApplicationCreateSchema(ApplicationBaseSchema):
    """Схема для создания заявки"""
    skills: List[SkillCreateSchema] | None
    work_format: List[WorkFormatCreateSchema]
    employment: List[EmploymentStyleCreateSchema]
    conditions: List[ConditionCreateSchema]
