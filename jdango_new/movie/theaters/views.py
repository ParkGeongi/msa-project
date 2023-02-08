from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from movie.theaters.repositories import TheaterRepository
from movie.theaters.serializers import TheaterSerializer


# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def theater(request):
        if request.method == 'POST':
                return TheaterSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return TheaterSerializer().update(request.data)
        elif request.method == 'DELETE':
                return TheaterSerializer().delete(request.data)
        elif request.method == 'GET':
                return TheaterRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def theater_list(request):
        return TheaterRepository().get_all()

