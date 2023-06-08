from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='home'),
    path('<slug>/', views.post_detail, name='post_detail'),
    #path('<slug:slug>/', views.post_detail, name='post_detail'),



    #path('<author_slug>/<slug:slug>/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:pk>/comment', views.post_comment, name='post_comment'),
]