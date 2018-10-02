from django.urls import path
from blog.views import articles, create_articles, articles_comment

urlpatterns = [
    path('', articles, name='blog_index'),
    path('create/',create_articles,  name='blog_create' ),
    path('comment_create/', articles_comment, name='blog_create_comment')
]