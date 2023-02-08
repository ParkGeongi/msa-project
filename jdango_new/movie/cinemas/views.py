from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from movie.cinemas.repositories import CinemasRepository
from movie.cinemas.serializers import CinemasSerializer


import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def cinemas(request):
        if request.method == 'POST':
                return CinemasSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return CinemasSerializer().update(request.data)
        elif request.method == 'DELETE':
                return CinemasSerializer().delete(request.data)
        elif request.method == 'GET':
                return CinemasRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def cinemas_list(request):
        return CinemasRepository().get_all()


