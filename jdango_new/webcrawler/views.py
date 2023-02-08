from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse, QueryDict
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from webcrawler.services import ScrapService


# Create your views here.
@api_view(["GET"])
@parser_classes([JSONParser])
def naver(request):

    #print(f"######## GET id is {request.GET['id']} ########")
    #index = int(request.GET['id']) -1
    a = ScrapService().naver_movie_review()

    print(f'GET 리턴 결과 : {a}')
    return JsonResponse(
        {'result': a})
