from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from movie.movies.models import Movies
from movie.movies.serializers import MoviesSerializer


class MovieRepository(object):

    def __init__(self):
        print(" CommentsRepository 객체 생성 ")

    def get_all(self):
        return Response(MoviesSerializer(Movies.objects.all(), many=True).data)

    def find_by_id(self,id):
        return Response(MoviesSerializer(Movies.objects.all(), many=True).data)