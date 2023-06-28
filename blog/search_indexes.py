import datetime
from core.settings import AUTH_USER_MODEL
from django.db import models
from haystack import indexes
from .models import Post


# class NoteIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
   
#     author = models.ForeignKey(AUTH_USER_MODEL, related_name='posts')
#     pub_date = indexes.DateTimeField(model_attr='pub_date')

#     def get_model(self):
#         return Note

#     def index_queryset(self, using=None):

#         return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
    



class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(AUTH_USER_MODEL, related_name='posts')

    def get_model(self):
        return Post

    def get_search_fields(self):
        return ('title', 'content')