from django import forms
from taggit.managers import TaggableManager
from .models import Post
# from .models import Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','content','image', 'status','tags', )
        prepopulated_fields = {'slug': ('title',)}
