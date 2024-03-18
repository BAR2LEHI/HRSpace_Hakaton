from datetime import datetime
from typing import List, Optional, Annotated
from pytz import timezone
from pydantic import BaseModel, model_validator, conint

from .enums import StatusEnum, FormatEnum, EmploymentEnum, PaperWorkEnum, ExperienceEnum, TypesResumeEnum, TermsPaymentEnum, TermsRecruiterEnum


class WorkFormatSchema(BaseModel):
    """Схема типа формата работы"""
    id: int
    title: str


class SkillSchema(BaseModel):
    """Схема навыка"""
    id: int
    name: str


class WorkFormatSchema(BaseModel):
    """Схема """
    id: int
    title: FormatEnum


class EmploymentStyleSchema(BaseModel):
    """Схема типа занятости соискателя"""
    id: int
    name: EmploymentEnum


class ApplicationSchema(BaseModel):
    """Схема заявки"""
    id: int
    title: str
    status: StatusEnum
    skills: Optional[List[SkillSchema]] | SkillSchema = None
    company_specialization: str
    work_format: List[WorkFormatSchema] | WorkFormatSchema
    address: Optional[str] = None
    experience: ExperienceEnum
    employment: List[EmploymentStyleSchema] | EmploymentStyleSchema
    salary_from: Optional[int] = None
    salary_up_to: Optional[int] = None
    paperwork: PaperWorkEnum
    responsibilities: Optional[str] = None
    requirements: Optional[str] = None
    conditions: Optional[str] = None
    payment: Annotated[int, conint(ge=1)]
    terms_payment: TermsPaymentEnum
    recruiters_number: Annotated[int, conint(ge=1, le=3)]
    resume_showing_date: datetime
    desired_release_date: datetime
    recruiter_responsibilities: Optional[str] = None
    resume_type: TypesResumeEnum
    terms_recruiter: TermsRecruiterEnum
    comments: Optional[str] = None
    stop_list_employee: Optional[str] = None

    @model_validator(mode='after')
    def check_salary_up(self):
        if self.salary_from > self.salary_up_to:
            raise ValueError('Максимальная планка зарплаты не может быть больше минимальной')
        return self

    # @model_validator(mode='after')
    # def check_date(self):
    #     date_now = datetime.now().astimezone(timezone('UTC'))
    #     if self.resume_showing_date < date_now or self.desired_release_date < date_now:
    #         raise ValueError('Не может быть указана дата ранее текущего дня')
    #     return self

    # class Config:
    #     orm_mode = True
