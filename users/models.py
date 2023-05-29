from django.db import models
from PIL import Image

# Create your models here.


# class User(models.Model):
#     username = models.CharField(max_length=200, blank=False)
#     email = models.EmailField(blank=False)
#     password = models.CharField(max_length=128)

#     class Meta:
#         ordering = ('username',)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     first_name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, blank=True)
#     location = models.CharField(max_length=200, blank=True)
#     image = models.ImageField(upload_to='profile_pics', default='default.jpg')

#     def __str__(self) -> str:
#         return self.first_name
    


     # override the save method in profile class and reduce the size of image size by the class
    # def save(self, **kwargs):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ('username',)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField()
    website = models.URLField()

    def __str__(self) -> str:
        return self.user.username

