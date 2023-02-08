from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token

from shop.deliveries.repositories import DeliveryRepository
from shop.deliveries.serializers import DeliverySerializer


# Create your views here.

@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def delivery(request):
        if request.method == 'POST':
                return DeliverySerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return DeliverySerializer().update(request.data)
        elif request.method == 'DELETE':
                return DeliverySerializer().delete(request.data)
        elif request.method == 'GET':
                return DeliveryRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def delivery_list(request):
        return DeliveryRepository().get_all()


