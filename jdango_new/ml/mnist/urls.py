from django.urls import re_path as url

from ml.mnist import views

urlpatterns = [

    url(r'fashion', views.fashion)

]