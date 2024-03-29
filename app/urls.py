"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


from manager.views import UserViewset, UserInfoViewSet
from user_operation.views import AW4ViewSet, A4ViewSet, CurReciteWords

router = SimpleRouter()
router.register('user', UserViewset, basename='user')
router.register('userinfo', UserInfoViewSet, basename='userinfo')
router.register('useraw', AW4ViewSet, basename='userw')
router.register('userlearned', A4ViewSet, basename='userlearned')
router.register('usercurlearned', CurReciteWords, basename='usercurlearned')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('', include('backend.urls')),
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),
]
