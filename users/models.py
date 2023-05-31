from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# function to create profile image path in the project
def get_profile_image_filepath(self, filename):
    return f"profile_images/{self.pk}/{'profile_image.png'}"

def get_default_profile_image():
    return "projectImages/default.jpg"


class CustomUser(AbstractUser):
    username = None  # remove the username field
    email = models.EmailField(_("email address"), unique=True) # make email field required and unique
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_image = models.ImageField(max_length=100, upload_to=get_profile_image_filepath, null=True, default=get_default_profile_image)
    location = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)

    # 
    USERNAME_FIELD = "email"  # set this field which defines the unique identifier for the User model to "email"
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager()  # specify that all objects for the class come from the CustomeUserManager

    def __str__(self) -> str:
        return self.email


