from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, user_name, password=None, **kwarg):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            password = password
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, user_name, password):
        user = self.create_user(email=email, user_name=user_name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    Id = models.AutoField(primary_key=True, unique=True,)
    email = models.EmailField(verbose_name='邮箱', unique=True, blank=False, max_length=255)
    user_name = models.CharField(verbose_name='用户名', max_length=20, unique=True)
    create_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    password = models.CharField(verbose_name='密码', max_length=100, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def  __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class CustomAuth:
    def authenticate(self, request, user_name=None, password=None):
        user = MyUser.objects.get(user_name=user_name)
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        user = MyUser.objects.get(Id=user_id)
        if user.is_active:
            return user
        return None
