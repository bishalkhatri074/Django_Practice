from django.urls import path
from cryptoc.views import index, about, contact, curriencies, github

urlpatterns = [
    path('crypto/',index, name='crypto_index'),
    path('about/', about, name='crypto_about'),
    path('contact/', contact, name= 'crypto_contact'),
    path("cur/", curriencies, name= 'crypto_curriencies'),
    path("git/", github, name='git_hub'),
]