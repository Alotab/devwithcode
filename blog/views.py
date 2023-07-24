from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
from .models import Post, Comment
# from users.models import CustomUser
from taggit.models import Tag
from .forms import PostForm
from .utilss import get_real_time_date_format




def post_blog(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      messages.success(request, 'Post created successfully')
      return redirect('blog:home')
      
  else:
    form = PostForm()
  return render(request, 'blog/createPost.html', {'form': form})




def post_list(request):
  """ List the all the post in the home page """
  posts = Post.published.all().order_by('-publish')
  # post_list = list(posts)
  trending_post = Post.published.all().order_by('-publish')[:6]
  latest_post = Post.published.all().order_by('-publish')[:3]
  tags = Tag.objects.all()

  context = {
    'posts': posts,
    'trending_post': trending_post,
    'tags': tags,
 
  }
  return render(request, 'blog/home.html', context)



def post_detail(request, slug, pk):
  post = get_object_or_404(Post, slug=slug, id=pk)
  comments = Comment.objects.filter(blog=post)
  post_tags = post.tags.all()
  trending_posts = Post.published.all().order_by('-publish')[:4]
  post_tags_id = post.tags.values_list('id', flat=True)
  related_posts = Post.published.filter(tags__in=post_tags_id).exclude(id=post.id)
  related_posts = related_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

  if request.method == 'POST':
    comment = Comment(
      user_comment=request.user,
      comment=request.POST['comment'],
      blog=post,
    )
    comment.save()
    # return redirect('/')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

  context = {
    'post': post,
    'comments': comments,
    'post_tags': post_tags,
    'related_posts': related_posts,
    'trending_posts': trending_posts,
  }
  return render(request, 'blog/post_detail.html', context)

