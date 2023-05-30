from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import get_user_model
from .forms import CustomeUserChangeForm, CustomUserCreationsForm
from django.views.generic.edit import CreateView
from django.core.exceptions import ValidationError
import re



def validate_email(email):
    regex = '^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'
    return re.match(regex, email)

def register(request):
    if request.method == 'POST':
        # username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if validate_email(email):
            # Create the user
            # user = User.objects.create(username=username, email=email, password=password)

            # Create the profile
            profile = CustomUser.objects.create( email=email, password=password)

            # Save the user and profile
            # user.save()
            profile.save()

            return redirect('home')
        else:
            return render(request, 'users/register.html', {'error': 'Invalid email address'})
    else:
        return render(request, 'users/register.html')
    



class RegistrationView(CreateView):
    form_class = CustomUserCreationsForm
    template_name = 'home.html'



    def form_valid(self, form_class):
            # Check if the password is strong enough
            if not form_class.cleaned_data['password'].isalnum() or len(form_class.cleaned_data['password']) < 8:
                raise ValidationError('Password must contain at least 8 characters and only letters and numbers.')

            # Check if the email address is already in use
            if CustomUser.objects.filter(email=form_class.cleaned_data['email']).exists():
                raise ValidationError('Email address already exists in the system.')

            # Create the user
            user = form_class.save()

            # Redirect to the success URL
            return super().form_valid(form_class)