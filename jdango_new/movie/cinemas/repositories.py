from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from movie.cinemas.models import Cinemas
from movie.cinemas.serializers import CinemasSerializer


class CinemasRepository(object):

    def __init__(self):
        print(" CinemaRepository 객체 생성 ")

    def get_all(self):
        return Response(CinemasSerializer(Cinemas.objects.all(), many=True).data)

    def find_by_id(self,id):
        return Response(CinemasSerializer(Cinemas.objects.all(), many=True).data)