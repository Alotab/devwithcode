from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomeUserChangeForm, UserCreationForm, CustomUserCreationsForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = CustomeUserChangeForm
    model = CustomUser
    list_display = ("email", "first_name", "last_name","is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name", "profile_image")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email", "first_name",)


admin.site.register(CustomUser, CustomUserAdmin)
