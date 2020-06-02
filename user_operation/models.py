from django.db import models
from django.contrib.auth import get_user_model

from backend.models import Cte4, Cte6

User = get_user_model()

class UserSaveWords(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    Cte4_words = models.ForeignKey(Cte4, verbose_name='保存4级的单词', on_delete=models.CASCADE)
    Cte6_words = models.ForeignKey(Cte6, verbose_name='保存6级的单词', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户保存错词'
