from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from movie.movies.repositories import MovieRepository
from movie.movies.serializers import MoviesSerializer

# Create your views here.
# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def movie(request):
        if request.method == 'POST':
                return MoviesSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return MoviesSerializer().update(request.data)
        elif request.method == 'DELETE':
                return MoviesSerializer().delete(request.data)
        elif request.method == 'GET':
                return MovieRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def movie_list(request):
        return MovieRepository().get_all()

