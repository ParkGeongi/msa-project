import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token

from shop.deliveries.models import Delivery
from shop.deliveries.serializers import DeliverySerializer


class DeliveryRepository(object):
    def __init__(self):
        pass


    def get_all(self):
        return Response(DeliverySerializer(Delivery.objects.all(), many=True).data)

    def find_by_id(self,id):
        pass

    def login(self, **keyargs):
        loginUser = Delivery.objects.get(user_email=keyargs['user_email'])

        if loginUser.password == keyargs["password"]:
            dbUser = Delivery.objects.all().filter(susers_id=loginUser.susers_id).values()[0]
            serializer = DeliverySerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
        else:
            return JsonResponse({'data': 'PASSWORD WRONG'})



