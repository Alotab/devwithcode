
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from users import views as user_views
# from haystack.views import SearchView
from core.sitemaps import (
    HomeSitemap,
    PostSitemap,
    PortfolioSitemap,
    CommentSitemap,
)

sitemaps = {
    "posts": PostSitemap,
    "home": HomeSitemap,
    "portfolio": PortfolioSitemap,
    "comment": CommentSitemap,
}


urlpatterns = [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap",
    ),
    path('admin/', admin.site.urls),

    path('signup/', user_views.account_signup_view, name='signup' ),
    # path('signin/', user_views.account_login_view, name='login'),
    path('home/', TemplateView.as_view(template_name='dash/homes.html'), name='homes'),
    path('accounts/', include('allauth.urls')),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name= 'logout'),
    path('portfolio/', user_views.portfolio, name= 'portfolio'),

    path('', include('blog.urls', namespace='blog')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
   

    ## Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
     name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
