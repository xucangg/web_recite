from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Cte4, Cte6, CountWords


class WdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cte4
        fields = '__all__'

class Wdcount(serializers.ModelSerializer):
    class Meta:
        model = CountWords
        fields = '__all__'
