from typing import Any, Optional
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# what this is doing is to set getting ride of the case insentive of the email logins/ 
# or making sure logins that contains captals are change to lower case because our backend is already implement a lower case email



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
        else:
            # this is just the login
            if user.check_password(password) and self.user_can_authenticate(user): 
                return user 
                     
        