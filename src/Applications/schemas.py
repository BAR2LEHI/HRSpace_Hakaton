from datetime import datetime
from typing import Annotated, List, Optional

from pydantic import BaseModel, conint, model_validator

from .enums import (EmploymentEnum, ExperienceEnum, FormatEnum, PaperWorkEnum,
                    TermsPaymentEnum, TermsRecruiterEnum, TypesResumeEnum)


class SkillCreateSchema(BaseModel):
    """Схема навыка"""
    name: str


class SkillGetSchema(SkillCreateSchema):
    id: int


class WorkFormatCreateSchema(BaseModel):
    """Схема """
    title: FormatEnum


class WorkFormatGetSchema(WorkFormatCreateSchema):
    id: int


class EmploymentStyleCreateSchema(BaseModel):
    """Схема типа занятости соискателя"""
    name: EmploymentEnum


class EmploymentStyleGetSchema(EmploymentStyleCreateSchema):
    id: int


class ApplicationBaseSchema(BaseModel):
    title: str
    company_specialization: str
    address: Optional[str] = None
    experience: ExperienceEnum
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
    stop_list_employee: Optional[str] = None

    @model_validator(mode='after')
    def check_salary_up(self):
        if self.salary_from > self.salary_up_to:
            raise ValueError('Максимальная планка зарплаты не может быть больше минимальной')
        return self
    
    class config:
        exclude = {'status'}


class ApplicationGetSchema(ApplicationBaseSchema):
    """Схема заявки"""
    id: int
    skills: Optional[List[SkillGetSchema]] = None
    work_format: List[WorkFormatGetSchema]
    employment: List[EmploymentStyleGetSchema]

    class config:
        orm_mode = True


class ApplicationCreateSchema(ApplicationBaseSchema):
    skills: List[SkillCreateSchema] | None
    work_format: List[WorkFormatCreateSchema]
    employment: List[EmploymentStyleCreateSchema]

    # @model_validator(mode='after')
    # def check_date(self):
    #     date_now = datetime.now().astimezone(timezone('UTC'))
    #     if self.resume_showing_date < date_now or self.desired_release_date < date_now:
    #         raise ValueError('Не может быть указана дата ранее текущего дня')
    #     return self

    # class Config:
    #     orm_mode = True
