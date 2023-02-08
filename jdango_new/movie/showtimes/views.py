from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from movie.showtimes.repositories import ShowtimeRepository
from movie.showtimes.serializers import ShowtimeSerializer
from security.seq_users.repositories import SeqUserRepository
from security.seq_users.serializers import SeqUserSerializer
from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def showtime(request):
        if request.method == 'POST':
                return ShowtimeSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return ShowtimeSerializer().update(request.data)
        elif request.method == 'DELETE':
                return ShowtimeSerializer().delete(request.data)
        elif request.method == 'GET':
                return ShowtimeRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def showtime_list(request):
        return ShowtimeRepository().get_all()


