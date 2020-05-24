from django.views.generic import TemplateView
from django.urls import path

from .views import WordList, AcountWords, Model, UserList, UserDetail


urlpatterns = [
    path('cte4/', WordList.as_view()),
    path('wordslength/', AcountWords.as_view()),
    path('model/', Model.as_view()),
    path('users', UserList.as_view()),
    path('users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]
