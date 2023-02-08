from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from ml.stroke.stroke import Stroke


# Create your views here.
@api_view(['POST'])
@parser_classes([JSONParser])
def stroke(request):
    Stroke().spec()
    return JsonResponse({'로그인 결과': 'SUCCESS'})