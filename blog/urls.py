from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('logins/', views.login, name='login')
]