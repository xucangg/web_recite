from django.db import models

class Cte4(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    en = models.CharField(max_length=50, verbose_name='english')
    ch = models.CharField(max_length=100, verbose_name='中文')
    category = models.CharField(max_length=10, verbose_name='分类')

    def __str__(self):
        return self.en

class Cte6(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    en = models.CharField(max_length=50, verbose_name='english', unique=True)
    ch = models.CharField(max_length=100, verbose_name='中文', unique=True)
    category = models.CharField(max_length=10, verbose_name='分类')

    def __str__(self):
        return self.en

class CountWords(models.Model):
    countcte4 = models.IntegerField(default=0, verbose_name='四级单词数')
    countcte6 = models.IntegerField(default=0, verbose_name='六级单词数')
    total = models.IntegerField(default=0, verbose_name='总数')
    