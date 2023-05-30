
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from users.models import CustomUser
from PIL import Image

# Create your models here.

#This manager filter the post objects to retreived on published post
class PublishedManager(models.Manager):
    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED)
    



class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=200)
    slug =  models.SlugField(max_length=250, unique_for_date='publish')
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post')
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="default.jpg", upload_to='post_pics')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()



    def __str__(self) -> str:
        return self.title


    # override the save method in post class and reduce the size of the image size
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (500, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse()
    



class Comments(models.Model):
    user_comment = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class CommentLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_likes')
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    # ensure that no two CommentLike objects have the same user and comment values.
    class Meta:
        unique_together = (('user', 'comment'),)
