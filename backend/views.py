from random import sample
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status


from backend.models import Cte4, Cte6, CountWords

#from manager.views import UserList
from manager.models import MyUser
from .serializers import WdSerializer, Wdcount

class WordList(ListCreateAPIView, RetrieveModelMixin, GenericAPIView):
    def get_queryset(self):
        if self.request.GET['type'] == 'cte4':
            cte4_words = Cte4.objects.all()
            return cte4_words
        if self.request.data['type'] == 'cte6':
            cte6_words = Cte6.objects.all()
            return cte6_words
    serializer_class = WdSerializer

class AcountWords(ListCreateAPIView, RetrieveModelMixin, GenericAPIView):
    queryset = CountWords.objects.all()
    serializer_class = Wdcount

class Model(ListCreateAPIView):

    def get_queryset(self):
        if self.request.GET['level'] == 'cte-4':
            c_words = Cte4.objects.all()
            word_random = sample(list(c_words), int(self.request.GET['num']))
            return word_random
        if self.request.GET['level'] == 'cte-6':
            c_words = Cte6.objects.all()
            word_random = sample(list(c_words), int(self.request.GET['num']))
            return word_random

    serializer_class = WdSerializer

#class UserLists(ListAPIView):
#    queryset = MyUser.objects.all()
#    serializer_class = UserList

#class UserDetail(RetrieveAPIView):
#    queryset = MyUser.objects.all()
#    serializer_class = UserList
