from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # get the custome user model 
from .forms import CustomeUserChangeForm, CustomUserCreationsForm, AccountAuthenticationForm
# from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
import re


def register(request, *args, **kwargs):
    user = request.user

    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}")
    context = {}

    if request.method == 'POST':
        form = CustomUserCreationsForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            # log_user = authenticate(email=email, password=raw_password)
            # login(request, log_user)
            # destination = get_redirect_if_exists(request) #kwargs.get('next')
            # if destination:
            #     redirect(destination)
            return redirect('home')
        else:
            context['custom_user_creations_form'] = form

    return render(request, "users/register.html", context)



# def login(request):
#     user = get_user_model()


# def login(request):
#     if request.method == 'POST':
#         # Get the username and password from the request.
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Try to authenticate the user.
#         user = authenticate(email=email, password=password)

#         # If the user is authenticated, log them in and redirect to the home page.
#         if user is not None:
#             login(request, user)
#             return redirect('home')

#         # Otherwise, show the login form again with errors.
#         else:
#             return render(request, 'users/login.html', {'errors': ['Invalid username or password.']})
#     return render(request, 'users/login.html')



def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('home')
        else:
            context['login_form'] = form
    return render(request, "users/login.html", context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect


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
    

# class RegisterView(CreateView):
#     model = get_user_model()
#     form_class = CustomUserCreationsForm
#     template_name = 'blog/home.html'
#     success_url = '/'
