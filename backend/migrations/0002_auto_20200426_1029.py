# Generated by Django 2.1.7 on 2020-04-26 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cte4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en', models.CharField(max_length=50, unique=True, verbose_name='english')),
                ('ch', models.CharField(max_length=100, unique=True, verbose_name='中文')),
                ('category', models.CharField(max_length=10, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Cte6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en', models.CharField(max_length=50, unique=True, verbose_name='english')),
                ('ch', models.CharField(max_length=100, unique=True, verbose_name='中文')),
                ('category', models.CharField(max_length=5, verbose_name='分类')),
            ],
        ),
        migrations.DeleteModel(
            name='Vocabulary',
        ),
    ]
