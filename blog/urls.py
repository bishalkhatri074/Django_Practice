from django.urls import path
from blog.views import articles, create_articles, articles_comment, blog_detail

urlpatterns = [
    path('', articles, name='blog_index'),
    path('create/',create_articles,  name='blog_create' ),
    path('comment_create/', articles_comment, name='blog_create_comment'),
    path('detail/<int:post_id>', blog_detail, name= 'blog_detail')
]