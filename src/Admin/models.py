from sqladmin import ModelView

from ..Users.models import User
from ..Applications.models import (
    Application, AppSkill, AppFormat,
    AppCondition, AppEmployment, Skill,
    Condition, WorkFormat, EmploymentStyle
)


class UserAdmin(ModelView, model=User):
    """Инициализация модели пользователя в админ-зоне"""
    column_list = [User.id, User.email]
    can_create = False
    category = "accounts"


class SkillAdmin(ModelView, model=Skill):
    """Инициализация модели скилла в админ-зоне"""
    category = "applications"
    column_list = [Skill.id, Skill.name]


class ConditionAdmin(ModelView, model=Condition):
    """Инициализация модели условий в админ-зоне"""
    category = "applications"
    column_list = '__all__'


class WorkFormatAdmin(ModelView, model=WorkFormat):
    """Инициализация модели формата работы в админ-зоне"""
    category = "applications"
    column_list = '__all__'


class EmploymentStyleAdmin(ModelView, model=EmploymentStyle):
    """Инициализация модели вида занятости в админ-зоне"""
    category = "applications"
    column_list = '__all__'


class AppSkillAdmin(ModelView, model=AppSkill):
    """Связь моделей сккиллов и заявок в админ-зоне"""
    category = 'applications'
    can_create = False
    column_list = '__all__'


class AppFormatAdmin(ModelView, model=AppFormat):
    """Связь моделей форматов и заявок в админ-зоне"""
    category = 'applications'
    can_create = False
    column_list = '__all__'


class AppConditionAdmin(ModelView, model=AppCondition):
    """Связь моделей условий и заявок в админ-зоне"""
    category = 'applications'
    can_create = False
    column_list = '__all__'


class AppEmploymentAdmin(ModelView, model=AppEmployment):
    """Связь моделей занятости и заявок в админ-зоне"""
    category = 'applications'
    can_create = False
    column_list = '__all__'


class ApplicationAdmin(ModelView, model=Application):
    """Инициализация модели заявки в админ-зоне"""
    category = 'applications'
    column_list = [
        Application.id, Application.title, Application.status,
        Application.desired_release_date
    ]
