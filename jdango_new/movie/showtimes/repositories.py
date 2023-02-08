import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from movie.showtimes.models import Showtime
from movie.showtimes.serializers import ShowtimeSerializer
from security.seq_users.models import SeqUser
from security.seq_users.serializers import SeqUserSerializer
from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token
class ShowtimeRepository(object):

    def __init__(self):
        print(" CommentsRepository 객체 생성 ")

    def get_all(self):
        return Response(ShowtimeSerializer(Showtime.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(ShowtimeSerializer(Showtime.objects.all(), many=True).data)