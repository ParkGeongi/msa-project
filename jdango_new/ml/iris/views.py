import json

from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from ml.iris.iris_model import IrisModel
from ml.iris.iris_service import IrisService
import tensorflow as tf

# Create your views here.
@api_view(['POST','GET'])
@parser_classes([JSONParser])
def iris(request):
    if request.method == 'POST':
        iris_data = json.loads(request.body)
        print(f'#################POST 리액트에서 보낸 데이터 : {iris_data}')
        SepalLengthCm = tf.constant(float(iris_data['SepalLengthCm']))
        SepalWidthCm = tf.constant(float(iris_data['SepalWidthCm']))
        PetalLengthCm = tf.constant(float(iris_data['PetalLengthCm']))
        PetalWidthCm = tf.constant(float(iris_data['PetalWidthCm']))
        print(f'POST 리액트에서 보낸 데이터 : {iris_data}')
        print(f'꽃받침의 길이 : {SepalLengthCm}')
        print(f'꽃받침의 너비 : {SepalWidthCm}')
        print(f'꽃잎의 길이: {PetalLengthCm}')
        print(f'꽃잎의 너비 : {PetalWidthCm}')

        result = IrisService().service_model([SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm])

        print(f'찾는 품종 : : {result}')
        if result == 0:
            resp = 'setosa / 부채붓꽃'
            print(resp)
        elif result == 1:
            resp = 'versicolor / 버시칼라 '
            print(resp)
        elif result == 2:
            resp = 'virginica / 버지니카'
            print(resp)

        return JsonResponse({'result': resp})
    elif request.method == 'GET':

        SepalLengthCm = float(request.GET['SepalLengthCm'])
        SepalWidthCm = float(request.GET['SepalWidthCm'])
        PetalLengthCm = float(request.GET['PetalLengthCm'])
        PetalWidthCm = float(request.GET['PetalWidthCm'])



        result = IrisService().service_model([SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm])
        print(f'찾는 품종 : : {result}')
        if result == 0:
            resp = 'setosa / 부채붓꽃'
            print(resp)
        elif result == 1:
            resp = 'versicolor / 버시칼라 '
            print(resp)
        elif result == 2:
            resp = 'virginica / 버지니카'
            print(resp)
        return JsonResponse({'result': resp})





