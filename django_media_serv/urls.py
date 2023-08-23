import django

if django.VERSION[0] >= 4:
    from django.urls import re_path
else:
    from django.conf.urls import url as re_path

from django_media_serv import views


urlpatterns = [
        re_path(r'^media/', views.getMediaFile, name='getMediaFile'),
]
