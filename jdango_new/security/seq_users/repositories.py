import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.seq_users.models import SeqUser
from security.seq_users.serializers import SeqUserSerializer
from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token



class SeqUserRepository(object):
    def __init__(self):
        pass


    def get_all(self):
        return Response(SeqUserSerializer(SeqUser.objects.all(), many=True).data)

    def find_by_id(self,id):
        return SeqUser.objects.all().filter(susers_id=id).values()[0]
    

    
    def login(self, **keyargs):
        loginUser = SeqUser.objects.get(user_email=keyargs['user_email'])

        if loginUser.password == keyargs["password"]:
            dbUser = self.find_by_id(loginUser.susers_id)
            serializer = SeqUserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
        else:
            return JsonResponse({'data': 'PASSWORD WRONG'})

    def find_user_by_email(self, param):
        return SeqUser.objects.all().filter(user_email=param).values()[0]

    def find_user_by_name(self, param):
        return SeqUser.objects.all().filter(job=param).values()

    def find_user_by_job(self, param):
        return SeqUser.objects.all().filter(job=param).values()

