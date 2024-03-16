from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .enums import *
from .models import EmploymentStyle, Skill, WorkFormat


class Application(BaseModel):
    """Схема заявки"""
    id: int
    title: str
    status: StatusEnum
    skills: Optional[List[Skill]] | Skill
    company_specialization: str
    work_format: List[WorkFormat] | WorkFormat
    address: Optional[str]
    experience: ExperienceEnum
    employment: EmploymentStyle
    salary_from: Optional[int]
    salary_up_to: Optional[int]
    paperwork: PaperWorkEnum
    responsibilities: Optional[str]
    requirements: Optional[str]
    conditions: Optional[str]
    payment: int
    terms_payment: TermsPaymentEnum
    recruiters_number: int
    resume_showing_date: datetime
    desired_release_date: datetime
    recruiter_responsibilities: Optional[str]
    resume_type: TypesResumeEnum
    terms_recruiter: TermsRecruiterEnum
    comments: Optional[str]
    stop_list_employee: Optional[str]


    class Meta:
        orm_mode = True
