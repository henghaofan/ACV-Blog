from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # blank=True  让用户在注册时无需填写昵称
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, blank=True)
    school = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True, default="这个人很懒，什么都没有留下")
    photo = models.ImageField(blank=True)

    class Meta(AbstractUser.Meta):
        pass
