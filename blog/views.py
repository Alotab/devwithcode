from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse
from django.views.generic.edit import FormMixin, FormView
from .models import Post, Comment
from users.models import CustomUser
from taggit.models import Tag
# from blog.forms import CommentForm

from users.forms import CommentForm




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
                   'tags': tags
                   })




class PostDetailView(DetailView):
    """ show the detail of a specific post """
    model = Post
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = lowercase_first_name(self.object.author)
        context['tags'] = self.object.tags.all()
        # context['comments'] = self.object.comment.all()
        context['comments'] = Comment.objects.filter(blog=self.object)
        context['pk'] = self.kwargs.get('pk')
        return context
    
def post_comment(request, pk):
  blog = Post.objects.get(pk=pk)
  comment = Comment(
    user_comment=request.user,
    comment =request.POST['comment'],
    blog=blog,
  )
  comment.save()
  return redirect('post_comment', pk=pk)


 



