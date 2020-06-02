from django.views.generic import TemplateView
from django.urls import path

from .views import WordList, AcountWords, Model


urlpatterns = [
    path('wordslist/', WordList.as_view()),
    path('wordslength/', AcountWords.as_view()),
    path('model/', Model.as_view())
]
