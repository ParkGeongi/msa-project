import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.seq_users.repositories import SeqUserRepository
from security.seq_users.serializers import SeqUserSerializer
from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def order(request):
        if request.method == 'POST':
                return SeqUserSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return SeqUserSerializer().update(request.data)
        elif request.method == 'DELETE':
                return SeqUserSerializer().delete(request.data)
        elif request.method == 'GET':
                return SeqUserRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def order_list(request):
        return SeqUserRepository().get_all()



