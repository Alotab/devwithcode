from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

from PIL import Image




class CustomUser(AbstractUser):
    username = None  # remove the username field
    email = models.EmailField(_("email address"), unique=True) # make email field required and unique

    # 
    USERNAME_FIELD = "email"  # set this field which defines the unique identifier for the User model to "email"
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager()  # specify that all objects for the class come from the CustomeUserManager

    def __str__(self) -> str:
        return self.email


