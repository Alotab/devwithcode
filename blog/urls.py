from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='home'),
    path('<author_slug>/<slug:slug>/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment', views.post_comment, name='post_comment'),
]