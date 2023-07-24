from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='home'),

    path('create/', views.post_blog, name='post'),
    path('<slug>-<int:pk>/', views.post_detail, name='post_detail'),
]