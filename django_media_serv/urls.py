from django import http, VERSION


from django.contrib import admin
from django.views.generic import TemplateView
from django_media_serv import views
from django.contrib.auth import logout, login
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings


if VERSION < (3, 0):
    from django.conf.urls import url, include
    urlpatterns = [
        url(r'^media/', views.getMediaFile, name='getMediaFile'),
    ]

else:
    from django.urls import re_path
    urlpatterns = [
            re_path(r'^media/', views.getMediaFile, name='getMediaFile'),
    ]




