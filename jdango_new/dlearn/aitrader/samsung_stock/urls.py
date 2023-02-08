from django.urls import re_path as url

from dlearn.aitrader.samsung_stock import views

urlpatterns = [
    url(r'samsung-stock',views.Samsung_stock)
]