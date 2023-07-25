from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from blog.models import Post
from blog.models import Comment


class HomeSitemap(Sitemap):
    changefreg = "daily"
    priority = 0.8

    def items(self):
        return ["home"]
    
    def location(self, item):
        return reverse(item)
    

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.publish 
    


class PortfolioSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ["portfolio"]
    
    def location(self, item):
        return reverse(item)


class CommentSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Comment.objects.all()
    
    def lastmod(self, obj):
        return obj.created_at



