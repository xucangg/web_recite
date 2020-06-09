from random import sample
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


from backend.models import Cte4, Cte6, CountWords

#from manager.views import UserList
from manager.models import MyUser
from .serializers import WdSerializer, Wdcount


class WordsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 20


class WordList(ListCreateAPIView, RetrieveModelMixin, GenericAPIView):

    def get_queryset(self):
        if self.request.GET['type'] == 'cte4':
            cte4_words = Cte4.objects.all()
            #c4_words = list(cte4_words)
            return cte4_words
        if self.request.GET['type'] == 'cte6':
            cte6_words = Cte6.objects.all()
            #c6_words = list(cte6_words)
            return cte6_words

    pagination_class = WordsPagination
    serializer_class = WdSerializer


class AcountWords(ListCreateAPIView, RetrieveModelMixin, GenericAPIView):
    queryset = CountWords.objects.all()
    serializer_class = Wdcount
    pagination_class = None

class ModePagination(PageNumberPagination):
    def get_paginated_response(self, data):
        random_words = []
        while len(data) > int(self.request.GET['num']):
            word_random = sample(list(data), int(self.request.GET['num']))
            random_words.extend(word_random)
            for i in word_random:
                data.remove(i)
        random_words.extend(data)
        return Response({
            'links':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link()
            },
            'count':self.page.paginator.count,
            'data':random_words
        })

    def get_page_size(self, request):
        return request.GET['num']

    max_page_size = 20
    page_size_query_param = 'page_size'


class Model(ListCreateAPIView):

    def get_queryset(self):
        if self.request.GET['level'] == 'Cte4':
            c_words = Cte4.objects.all()
            return c_words
        if self.request.GET['level'] == 'Cte6':
            c_words = Cte6.objects.all()
            return c_words



    serializer_class = WdSerializer
    pagination_class = ModePagination

#class UserLists(ListAPIView):
#    queryset = MyUser.objects.all()
#    serializer_class = UserList

#class UserDetail(RetrieveAPIView):
#    queryset = MyUser.objects.all()
#    serializer_class = UserList
