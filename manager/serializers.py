from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from backend.models import Cte4, Cte6
from .models import MyUser

class UserSerializer(ModelSerializer):
    #words = serializers.PrimaryKeyRelatedField(many=True, queryset=Cte4.objects.all())
    class Meta:
        model = MyUser
        fields = '__all__'
    