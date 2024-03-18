from enum import Enum


class StatusEnum(str, Enum):
    """Список доступных статусов заявки"""
    approved = 'approved'
    moderation = 'moderation'
    draft = 'draft'
    close = 'close'


class FormatEnum(str, Enum):
    """Список доступных форматов работы"""
    office = 'office'
    hybrid = 'hybrid'
    remotely_rf = 'remotely_rf'
    remotely_world = 'remotely_world'


class ExperienceEnum(str, Enum):
    """Список доступного выбора опыта работы"""
    without_exp = 'without_exp'
    up_to_one_year = 'up_to_one_year'
    from_one_year = 'from_one_year'
    from_2_years = 'from_2_years'
    from_3_years = 'from_3_years'


class EmploymentEnum(str, Enum):
    """Список доступного выбора занятости"""
    full_time ='full_time'
    part_time = 'part_time'
    project_activities = 'project_activities'


class PaperWorkEnum(str, Enum):
    """Условия сотрудничества со соискателем"""
    gph = 'gph'
    fixed_term = 'fixed_term'
    full_registration = 'full_registration'


class TermsPaymentEnum(str, Enum):
    """Условия оплаты работы рекрутера"""
    all_now = 'all_now'
    fifty_fifty = 'fifty_fifty'
    all_after = 'all_after'


class TypesResumeEnum(str, Enum):
    """Виды резюме"""
    no_interview = 'no_interview'
    with_interview = 'with_interview'


class TermsRecruiterEnum(str, Enum):
    """Условия сотрудничества с рекрутером"""
    gph = 'gph'
    agreement_with_legal_entity = 'agreement_with_legal_entity'
