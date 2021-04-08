import datetime
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from backend.serializers import WdSerializer
from  manager.models import UserInfo
from .models import AddWrongWordsCte4, UserLearnedWordsCte4
from .serializers import AW4Serializer, A4Serializer, Cte4Serializer, RCte4Serializer


WORDS_TYPE = ['cte4', 'cte6']

#添加错误和展示四级单词
class AW4ViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_info = UserInfo.objects.filter(inner_id_id=self.request.user )
        word_num = AddWrongWordsCte4.objects.filter(user=self.request.user).count()
        user_info.update(wrong_4words_num=word_num)
        cte4_num = user_info.get().wrong_4words_num
        cte6_num = user_info.get().wrong_6words_num
        user_info.update(total_wrong_words=cte4_num+cte6_num)
        return Response('save success')

    def get_serializer_class(self):
        if self.action == 'create':
            return AW4Serializer
        if self.action == 'list':
            return Cte4Serializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return AddWrongWordsCte4.objects.filter(user=self.request.user)

#添加已学和展示
class A4ViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_info = UserInfo.objects.filter(inner_id_id=self.request.user )
        word_num = UserLearnedWordsCte4.objects.filter(user=self.request.user).count()
        user_info.update(learned_cte4_num=word_num)
        cte4_num = user_info.get().learned_cte4_num
        cte6_num = user_info.get().learned_cte6_num
        user_info.update(total_learned_num=cte4_num+cte6_num)
        return Response('save success')

    def get_serializer_class(self):
        if self.action == 'create':
            return A4Serializer
        if self.action == 'list':
            return RCte4Serializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return UserLearnedWordsCte4.objects.filter(user=self.request.user)

#近期默写单词
class CurReciteWords(viewsets.GenericViewSet, ListModelMixin):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = RCte4Serializer

    def get_queryset(self):
        three_days = datetime.datetime.now()+datetime.timedelta(days=-3)
        current_words = UserLearnedWordsCte4.objects.filter(user=self.request.user, learn_time__gte=three_days)
        return current_words