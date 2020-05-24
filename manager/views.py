from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import MyUser
from .serializers import UserSerializer


class UserList(APIView):

    def get(self, request):
        user = MyUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
