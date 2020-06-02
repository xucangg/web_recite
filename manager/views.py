from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler


from .serializers import UserSerializer, UserRegSerializer
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

class UserViewset(CreateModelMixin, viewsets.GenericViewSet, RetrieveModelMixin):

    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserSerializer
        if self.action == 'create':
            return UserRegSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)

        return Response(re_dict)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()
