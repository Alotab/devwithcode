from typing import Any, Optional
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest


class CaseInsentiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        userModel = get_user_model()

        if username is None:
            username = kwargs.get(userModel.USERNAME_FIELD)

        try:
            case_insentive_username_field = '{}__iexact'.format(userModel.USERNAME_FIELD)
            user = userModel._default_manager.get(**{case_insentive_username_field: username})
        except userModel.DoesNotExist:
            userModel().set_password(password)
                     
        