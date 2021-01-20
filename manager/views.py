from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework import mixins, viewsets, status, authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BaseAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_decode_handler, jwt_payload_handler

from .models import UserInfo
from .serializers import UserSerializer, UserRegSerializer, InfoSerializer
User = get_user_model()

class CustomAuth(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.get(email=username)
        if user.check_password(password):
            return user
        return None

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username
    }


class UserViewset(CreateModelMixin, viewsets.GenericViewSet, ):

    serializer_class = UserRegSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        user_data = User.objects.get(username=request.data['username'])
        user_info = UserInfo(inner_id=user_data)
        user_info.save()
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        return Response(re_dict)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()

class UserInfoViewSet(GenericViewSet, ListModelMixin):
    serializer_class = InfoSerializer
    authentication_classes = [JSONWebTokenAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserInfo.objects.filter(inner_id=self.request.user)
