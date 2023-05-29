from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
from .models import Profile, User
import re



def validate_email(email):
    regex = '^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'
    return re.match(regex, email)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if validate_email(email):
            # Create the user
            user = User.objects.create(username=username, email=email, password=password)

            # Create the profile
            profile = Profile.objects.create(user=user)

            # Save the user and profile
            user.save()
            profile.save()

            return redirect('home')
        else:
            return render(request, 'users/register.html', {'error': 'Invalid email address'})
    else:
        return render(request, 'users/register.html')
    



def login(request):
    return render(request, 'blog/try.html')