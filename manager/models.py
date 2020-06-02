from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):

    Id = models.AutoField(primary_key=True, unique=True,)
    email = models.EmailField(verbose_name='邮箱', unique=True, blank=False, max_length=255)
    username = models.CharField(verbose_name='用户名', max_length=20, unique=True)
    create_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    class Meta:
        verbose_name = '用户'

    def __str__(self):
        return self.username
