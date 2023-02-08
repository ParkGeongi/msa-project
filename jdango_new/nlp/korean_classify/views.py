from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from nlp.naver_movie.services import ReviewService

import json

# Create your views here.

@api_view(["POST"])
@parser_classes([JSONParser])
def korean_claasifyviews(request):

    return JsonResponse({'result': 'data'})
