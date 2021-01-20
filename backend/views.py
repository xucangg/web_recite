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

    def get_page_size(self, request):
        return request.GET['num']

    max_page_size = 20
    page_size_query_param = 'page_size'

class Model(ListCreateAPIView):
    def get_queryset(self):
        if self.request.GET['level'] == 'Cte4':
            if self.request.GET['model'] == 'random':
                r_words = Cte4.objects.order_by('?')
                return r_words
            if self.request.GET['model'] == 'initial':
                i_words = Cte4.objects.order_by('en')
                return i_words
        if self.request.GET['level'] == 'Cte6':
            if self.request.GET['model'] == 'random':
                r_words = Cte4.objects.order_by('?')
                return r_words
            if self.request.GET['model'] == 'initial':
                i_words = Cte6.objects.order_by('en')
                return i_words

    serializer_class = WdSerializer
    pagination_class = ModePagination
