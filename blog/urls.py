from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='home'),
    # path('<int:pk>/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail')
   # path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail')
    
    
    # path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail')



     path('<author_slug>/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
]