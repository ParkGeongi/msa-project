from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from blog.tags.repositories import TagRepository
from blog.tags.serializers import TagSerializer
from security.seq_users.repositories import SeqUserRepository

from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def tag(request):
        if request.method == 'POST':
                return TagSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return TagSerializer().update(request.data)
        elif request.method == 'DELETE':
                return TagSerializer().delete(request.data)
        elif request.method == 'GET':
                return TagRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def tag_list(request):
        return SeqUserRepository().get_all()


