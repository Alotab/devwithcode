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
    text = indexes.CharField(document=True, use_template=True)
    content = indexes.CharField(model_attr="content")


    # content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Post
    
    def index_queryset(self, using=None):
        '''Used when the entire index for model is'''
        return self.get_model().objects.all()

    def get_search_fields(self):
        return ('title', 'content')
    

    def __init__(self, *args, **kwargs):
        if 'document' in kwargs:
            del kwargs['document']
        super().__init__(*args, **kwargs)
    
