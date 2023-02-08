from django.urls import re_path as url

from ml.stroke import views

urlpatterns = [
    url(r'stroke', views.stroke),
]