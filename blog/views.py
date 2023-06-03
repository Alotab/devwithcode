from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView
from .models import Post, CommentLike, Comments

# Create your views here.



def post_list(request):
    """ List the all the post in the home page """
    posts = Post.published.all()
    trending_post = Post.published.all().order_by('-publish')[:6]
    return render(request, 'blog/home.html', {'posts': posts, 'trending_post': trending_post})



class PostDetailView(DetailView):
    """ show the detail of a specific post """
    model = Post
    template_name = 'blog/post_detail.html'