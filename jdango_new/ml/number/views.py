from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse, QueryDict
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from ml.number.number_service import NumberService


# Create your views here.
@api_view(["POST","GET"])
@parser_classes([JSONParser])
def number(request):
    if request.method == 'POST':
        id = json.loads(request.body)
        print(f"######## POST id is {id} type is {type(id)} ########")
        a = NumberService().service_model(int(id))
        print(f'POST 리턴 결과 : {a}')
        return JsonResponse({'result' : a})
    elif request.method == 'GET':

        print(f"######## GET id is {request.GET['id']} ########")
        a = NumberService().service_model(int(request.GET['id']))
        print(f'GET 리턴 결과 : {a}')
        return JsonResponse(
            {'result': a})

    else:
        print(f"######## ID is None ########")