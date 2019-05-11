from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'article'  # 一定要写这一行，否则html中会报错 'article' is not a registered namespace

urlpatterns = [
    path(r'article_post/', views.article_post, name='article_post'),
    path(r'article_list/', views.article_list, name='article_list'),
    path(r'article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path(r'like_article/', views.like_article, name='like_article'),
]
