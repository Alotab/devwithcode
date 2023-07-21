from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
# from django.views.generic import DetailView
from django.urls import reverse
# from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
# from users.models import CustomUser
from taggit.models import Tag
from .forms import PostForm

from haystack.models import SearchResult
from haystack.query import SearchQuerySet
from .utilss import get_real_time_date_format
from django.db.models import Count
from django.core.paginator import Paginator
from chatbot_model import quesans
from django.contrib import messages

# from blog.forms import CommentForm
# from users.forms import CommentForm


def post_blog(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    # print(form.errors)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      messages.success(request, 'Post created successfully')
      return redirect('blog:home')
      
  else:
    form = PostForm()
  return render(request, 'blog/createPost.html', {'form': form})



# def lowercase_first_name(author_first_name):
#     return str(author_first_name).lower()



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



def search_titles(request):
  post = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))

  return render('search.html', {'post': post})


# chatbot
# def chatbotresponse(request):
#   question = request.GET['question']

#   res = quesans(question)
#   return res

# chtabot
# def post_fetch(request):
#   total_item = int(request.GET.get('total_item'))
#   limit = 5
#   post_obj = list(Post.objects.values()[total_item:total_item+limit])
#   data={
#     'posts':post_obj
#   }
#   return JsonResponse(data=data)




# class PostDetailView(DetailView):
#     """ show the detail of a specific post """
#     model = Post
#     template_name = 'blog/post_detail.html'
#     slug_field = 'slug'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author'] = lowercase_first_name(self.object.author)
    #     context['tags'] = self.object.tags.all()
    #     # context['comments'] = self.object.comment.all()
    #     context['comments'] = Comment.objects.filter(blog=self.object)
    #     context['pk'] = self.kwargs.get('pk')
    #     return context
    

# def post_comment(request, slug):
#     blog = Post.objects.get(slug=slug)
#     if request.method == 'POST':
#       comment = Comment(user_comment=request.user,comment =request.POST['comment'],blog=blog,)
#       comment.save()
#       return redirect('blog:home')
#     return 
    
# def post_comment(request, pk):
#   slug = request.resolver_match.kwargs.slug
#   blog = Post.objects.get(slug=slug)
  ##blog = Post.objects.get(pk=pk)
#   comment = Comment(
#     user_comment=request.user,
#     comment =request.POST['comment'],
#     blog=blog,
#   )
#   comment.save()
#   return redirect('blog:post-detail', args=[blog.pk])

  #return redirect('blog:post-detail', args=[blog.pk])
  #return redirect(reverse('blog:post-detail', args=(blog.pk,)))
#   return redirect(reverse('blog:post-detail', args=(pk,)))
  #return redirect('blog:post-detail', pk=str(pk))


# def post_comment(request):
#   slug = request.resolver_match.kwargs.get('slug')
#   if slug is not None:
#     blog = Post.objects.get(slug=slug)
#     comment = Comment(
#       user_comment=request.user,
#       comment =request.POST['comment'],
#       blog=blog,
#     )
#     comment.save()
#     return redirect('blog:post-detail', args=[blog.pk])
#   else:
#     return redirect('home')



# def post_comment(request):
#   slug = request.resolver_match.kwargs.get('slug')
#   if slug is not None:
#     blog = Post.objects.get(slug=slug)
#     comment = Comment(
#       user_comment=request.user,
#       comment =request.POST['comment'],
#       blog=blog,
#     )
#     comment.save()
#     return redirect('blog:post-detail')
#   else:
#     return redirect('home')


# def post_comment(request):
#   slug = request.resolver_match.kwargs.get('slug')
#   if slug is not None:
#     blog = Post.objects.get(slug=slug)
#     comment = Comment(
#       user_comment=request.user,
#       comment =request.POST['comment'],
#       blog=blog,
#     )
#     comment.save()
#     return redirect('blog:post-detail', args=[blog.pk])
#   else:
#     return redirect('home')