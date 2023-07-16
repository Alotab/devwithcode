from django.urls import path
from haystack.views import SearchView
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='home'),
    path('fetch/', views.post_fetch, name='fetch'),

    path('create/', views.post_blog, name='post'),
    # path('<slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>-<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.search_titles, name='search'),
   
    #path('<slug:slug>/', views.post_detail, name='post_detail'),
    
    #path('<author_slug>/<slug:slug>/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:pk>/comment', views.post_comment, name='post_comment'),
]



