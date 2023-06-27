
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings
from django.http import Http404
from django.utils.text import slugify
from django.db.models.signals import pre_save
from PIL import Image
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# This manager filter the post objects to retreived on published post
class PublishedManager(models.Manager):
    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED)
    
# class PublishedManager(models.Manager):

#   def get_queryset(self):
#     return Post.objects.filter(status=Post.Status.PUBLISHED)

#   def get_or_404(self, slug):
#     try:
#       return self.get(slug=slug)
#     except Post.DoesNotExist:
#       raise Http404("Post does not exist")

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=200)
    slug =  models.SlugField(max_length=250, unique_for_date='publish', unique=True, blank=True)
    # content = models.TextField()
    # content = RichTextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    # content = RichTextUploadingField(config_name='awesome_ckeditor')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post')
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="default.jpg", upload_to='post_pics')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()


    def __str__(self) -> str:
        return self.title
    

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])
    

    def create_slug(sender, instance, **kwargs):
        if not instance.slug:
            instance.slug = slugify(instance.title)



    # override the save method in post class and reduce the size of the image size
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (500, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
        # if not self.slug:
        #     self.slug = slugify(self.title)
    



class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user_comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user_comment} {self.blog}'



class CommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    # ensure that no two CommentLike objects have the same user and comment values.
    class Meta:
        unique_together = (('user', 'comment'),)
