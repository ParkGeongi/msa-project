from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token

from shop.products.repositories import ProductRepository
from shop.products.serializers import ProductSerializer


@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def product(request):
        if request.method == 'POST':
                return ProductSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return ProductSerializer().update(request.data)
        elif request.method == 'DELETE':
                return ProductSerializer().delete(request.data)
        elif request.method == 'GET':
                return ProductRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def product_list(request):
        return ProductRepository().get_all()



