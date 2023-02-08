from django.urls import re_path as url

from shop.carts import views

urlpatterns = [
    url(r'cart',views.Cart),
    url(r'list',views.Cart_list)
]