from django import forms
from taggit.managers import TaggableManager
from .models import Post



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','content','image', 'status','tags', )
        prepopulated_fields = {'slug': ('title',)}
