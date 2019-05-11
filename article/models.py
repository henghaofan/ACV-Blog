from django.db import models

# Create your models here.

from django.db import models
from users.models import User
from django.utils import timezone
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article", null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    users_like = models.ManyToManyField(User, related_name="articles_like", blank=True)

    class Meta:
        ordering = ("-updated",)

    # 对数据库中的这两个字段建立索引，以后就可以通过每篇文章的id和slug来获取该文章对象了，
    # 这样建立索引以后，能提高读取文章对象的速度。
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentator", null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "Comment by {0} on {1}".format(self.commentator.username, self.article)
