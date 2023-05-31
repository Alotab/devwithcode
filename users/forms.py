from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django import forms



# class CustomUserCreationsForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("email",)



class CustomUserCreationsForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False #Send  confirmation email
        if commit:
            user.save()
        return user



class CustomeUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)