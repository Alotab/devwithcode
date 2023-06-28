from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
# from django.views.generic import DetailView
from django.urls import reverse
# from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
# from users.models import CustomUser
from taggit.models import Tag
from .forms import PostForm

from haystack.models import SearchResult

# from blog.forms import CommentForm
# from users.forms import CommentForm


def post_blog(request):
  if request.method == 'POST':
    form = PostForm(request.POST)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('blog:home')
      
  else:
    form = PostForm()
  return render(request, 'blog/createPost.html', {'form': form})

# @login_required
# def post_blog(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         slug = request.POST['slug']
#         posts = Post.objects.create(
#             title=title,
#             content=content,
#             author=request.user
#         )
#         posts.save()
#         return redirect('blog:home')
#     else:
#         return render(request, 'blog/createPost.html')


def lowercase_first_name(author_first_name):
    return str(author_first_name).lower()



def post_list(request):
    """ List the all the post in the home page """
    posts = Post.published.all().order_by('-publish')
    trending_post = Post.published.all().order_by('-publish')[:6]
    latest_post = Post.published.all().order_by('-publish')[:3]
    tags = Tag.objects.all()

    return render(request, 
                  'blog/home.html', 
                  {'posts': posts, 
                   'trending_post': trending_post,
                   'tags': tags,
                   })


def post_detail(request, slug):
 
  blog = get_object_or_404(Post, slug=slug)
  comments = Comment.objects.filter(blog=blog)
  post_tags = blog.tags.all()

  # author = blog.author
  # first_name = author.get_short_name()
  # slug = f"{first_name}/{slug}"

  if request.method == 'POST':
    comment = Comment(
      user_comment=request.user,
      comment=request.POST['comment'],
      blog=blog,
    )
    comment.save()
    # return redirect('/')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

  context = {
    'blog': blog,
    'comments': comments,
    'post_tags': post_tags,
  }
  return render(request, 'blog/post_detail.html', context)



# class PostDetailView(DetailView):
#     """ show the detail of a specific post """
#     model = Post
#     template_name = 'blog/post_detail.html'
#     slug_field = 'slug'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['author'] = lowercase_first_name(self.object.author)
#         context['tags'] = self.object.tags.all()
#         # context['comments'] = self.object.comment.all()
#         context['comments'] = Comment.objects.filter(blog=self.object)
#         context['pk'] = self.kwargs.get('pk')
#         return context
    

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