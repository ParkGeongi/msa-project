import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.seq_users.serializers import SeqUserSerializer
from rest_framework.authtoken.models import Token

from shop.products.models import Product
from shop.products.serializers import ProductSerializer




class ProductRepository(object):
    def __init__(self):
        pass


    def get_all(self):
        return Response(ProductSerializer(Product.objects.all(), many=True).data)

    def find_by_id(self,id):
        pass




