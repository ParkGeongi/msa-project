import json
from django.http import JsonResponse, QueryDict
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf
from rest_framework.response import Response
from ml.mnist.fashion_service import FashionService
# Create your views here.
@api_view(["POST","GET"])
@parser_classes([JSONParser])
def fashion(request):
    if request.method == 'POST':
        id = json.loads(request.body)
        print(f"######## POST id is {id} type is {type(id)} ########")
        a = FashionService().service_model(int(id))
        print(f'POST 리턴 결과 : {a}')
        return JsonResponse({'result' : a})
    elif request.method == 'GET':

        print(f"######## GET id is {request.GET['id']} ########")
        a = FashionService().service_model(int(request.GET['id']))
        print(f'GET 리턴 결과 : {a}')
        return JsonResponse(
            {'result': a})

        '''
        data = request.data
        test_num = tf.constant(int(data['test_num']))
        result = FashionService().service_model([test_num])
        return JsonResponse({'result': result})
'''



    else:
        print(f"######## ID is None ########")