from django.db import models
from django.contrib.auth import get_user_model
from backend.models import Cte4, Cte6

from time import ctime

User = get_user_model()

class AddWrongWordsCte4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    save_cte4_words = models.ForeignKey(Cte4, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

class AddWrongWordsCte6(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    save_cte6_words = models.ForeignKey(Cte6, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True) 

class UserLearnedWordsCte4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cte4 = models.ForeignKey(Cte4, on_delete=models.CASCADE)
    learn_time = models.DateTimeField(auto_now_add=True,)

class UserLearnedWordsCte6(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cte6 = models.ForeignKey(Cte6, on_delete=models.CASCADE)
    learn_time = models.DateTimeField(auto_now_add=True)
