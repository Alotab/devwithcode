from django import forms
from taggit.managers import TaggableManager
from .models import Post
# from .models import Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')



class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=300)
    # content = forms.Textarea()
    # slug = forms.SlugField()
    # image = forms.ImageField()
    
    # tag = TaggableManager()
    

    class Meta:
        model = Post
        fields = ('title','content', 'image', 'author', 'status','tags', )
        prepopulated_fields = {'slug': ('title',)}
        # fields = '__all__'
        # exclude = ('author', 'slug',)
