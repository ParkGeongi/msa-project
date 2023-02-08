from django.urls import re_path as url

from ml.number import views

urlpatterns = [

    url(r'number', views.number)

]