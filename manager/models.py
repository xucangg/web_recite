import random
import uuid
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

class UserInfo(models.Model):
    GENDER_CHOICES = (
        ('male', u'男'),
        ('female', u'女')
    )

    inner_id = models.OneToOneField(MyUser, on_delete=models.CASCADE,)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    is_member = models.CharField(max_length=1, default='0')
    learned_cte4_num = models.IntegerField(default=0)
    learned_cte6_num = models.IntegerField(default=0)
    wrong_4words_num = models.IntegerField(default=0)
    wrong_6words_num = models.IntegerField(default=0)   
    total_learned_num = models.IntegerField(default=0)
    total_wrong_words = models.IntegerField(default=0)
    current_learn_cte4 = models.IntegerField(default=0)
    current_learn_cte6 = models.IntegerField(default=0)

    class Meta:
        verbose_name = '用户信息'
