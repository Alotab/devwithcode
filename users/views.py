from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import get_user_model  # get the custome user model 
from .forms import CustomeUserChangeForm, CustomUserCreationsForm
from django.views.generic import CreateView, FormView
from django.core.exceptions import ValidationError
import re


def register(request, *args, **kwargs):
    user = request.user

    # if user.is_authenticated:
    #     return HttpResponse(f"You are already authenticated as {user.email}")
    context = {}

    if request.method == 'POST':
        form = CustomUserCreationsForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            # customUser = authenticate(email=email, password=raw_password)
            # login(request, customUser)
            destination = kwargs.get('next')
            if destination:
                redirect(destination)
            return redirect('home')
        else:
            context['custom_user_creations_form'] = form

    return render(request, "users/register.html", context)





# def validate_email(email):
#     regex = '^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'
#     return re.match(regex, email)

# def register(request):
#     if request.method == 'POST':
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']

        # if validate_email(email):
            # Create the user
            # user = User.objects.create(username=username, email=email, password=password)

            # Create the profile
            # profile = CustomUser.objects.create( email=email, password=password)

            # Save the user and profile
            # user.save()
            # profile.save()

    #         return redirect('home')
    #     else:
    #         return render(request, 'users/register.html', {'error': 'Invalid email address'})
    # else:
    #     return render(request, 'users/register.html')
    

class RegisterView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationsForm
    template_name = 'blog/home.html'
    success_url = '/'
