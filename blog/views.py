from django.shortcuts import render, HttpResponse
from .models import Post, CommentLike, Comments

# Create your views here.



def post_list(request):
    posts = Post.published.all()
    trending_post = Post.published.all().order_by('-publish')[:6]
    return render(request, 'blog/home.html', {'posts': posts, 'trending_post': trending_post})
