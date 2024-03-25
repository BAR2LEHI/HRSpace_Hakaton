from sqladmin import ModelView

from ..Users.models import User
from ..Applications.models import (
    Application, AppSkill, AppFormat,
    AppCondition, AppEmployment, Skill,
    Condition, WorkFormat, EmploymentStyle
)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]
    can_create = False
    category = "accounts"


class SkillAdmin(ModelView, model=Skill):
    category = "applications"
    column_list = [Skill.id, Skill.name]


class ConditionAdmin(ModelView, model=Condition):
    category = "applications"
    column_list = '__all__'


class WorkFormatAdmin(ModelView, model=WorkFormat):
    category = "applications"
    column_list = '__all__'


class EmploymentStyleAdmin(ModelView, model=EmploymentStyle):
    category = "applications"
    column_list = '__all__'


'''class ApplicationAdmin(ModelView, model=Application):
    column_list = '__all__'
    category = "applications"'''


class AppSkillAdmin(ModelView, model=AppSkill):
    category = 'applications'
    can_create = False
    column_list = '__all__'



class AppFormatAdmin(ModelView, model=AppFormat):
    category = 'applications'
    can_create = False
    column_list = '__all__'


class AppConditionAdmin(ModelView, model=AppCondition):
    category = 'applications'
    can_create = False
    column_list = '__all__'


class AppEmploymentAdmin(ModelView, model=AppEmployment):
    category = 'applications'
    can_create = False
    column_list = '__all__'


class ApplicationAdmin(ModelView, model=Application):
    category = 'applications'
    column_list = [
        Application.id, Application.title, Application.status,
        Application.desired_release_date
    ]
    '''form_ajax_refs = {
        'skills': {
            'fields': ('name',),
        }
    }'''
