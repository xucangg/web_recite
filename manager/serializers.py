from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from backend.models import Cte4, Cte6
from manager.models import MyUser

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password')

    username = serializers.CharField(
        label='用户名',
        required=True,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all(), message='用户名已被注册')]
    )

    email = serializers.EmailField(
        label='邮箱',
        required=True,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all(), message='邮箱已被注册')]
        )

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
    