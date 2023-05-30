from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser



class CustomUserCreationsForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)



class CustomeUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)