from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView
from django.urls import reverse
# from django.utils.
from .models import Post, CommentLike, Comments
from users.models import CustomUser
from taggit.models import Tag




def lowercase_first_name(author_first_name):
    return str(author_first_name).lower()

# def get_author_slug_url(author_name, slug):
#     url = reverse('post-detail', args=[author_name, slug])
#     return url

def post_list(request):
    """ List the all the post in the home page """
    posts = Post.published.all()
    trending_post = Post.published.all().order_by('-publish')[:6]
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
        return context
    