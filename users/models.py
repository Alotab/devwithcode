from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
# from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# function to create profile image path in the project
def get_profile_image_filepath(self, filename):
    return f"profile_images/{self.pk}/{'profile_image.png'}"

def get_default_profile_image():
    return "projectImages/default.jpg"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    #username = models.CharField(max_length=100, null=True,unique=True, blank=True)  # remove the username field
    email = models.EmailField(_("email address"), unique=True) # make email field required and unique
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_image = models.ImageField(max_length=100, upload_to=get_profile_image_filepath, null=True, default=get_default_profile_image)
    location = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_supperuser = models.BooleanField(default=False)


    # 
    USERNAME_FIELD = "email"  # set this field which defines the unique identifier for the User model to "email"
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager()  # specify that all objects for the class come from the CustomeUserManager

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_login}"
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    # def get_full_name(self):
    #     return f"{self.first_name} {self.last_login}"
    
    def get_short_name(self):
        return f"{self.first_name}"
    
    
    # change the name of profile image to the default name
    def get_profile_image_filename(self):
        return str(self.profile_iamge)[str(self.profile_image).index(f"profile_images/{self.pk}/"):]



