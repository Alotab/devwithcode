from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import authenticate
from django import forms
from .models import CustomUser


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
        fields = '__all__'
        # fields = ("email","first_name", "last_name",)



# building this from scratch for the userauthentication

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput) # to hide the password when typing

    class Meta:
        model = CustomUser
        fields = ("email", "password")

    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")