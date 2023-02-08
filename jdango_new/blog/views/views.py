from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from blog.views.repositories import ViewRepository
from blog.views.serializers import ViewSerializer
from security.seq_users.repositories import SeqUserRepository
from security.seq_users.serializers import SeqUserSerializer

# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def view(request):
        if request.method == 'POST':
                return ViewSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return ViewSerializer().update(request.data)
        elif request.method == 'DELETE':
                return ViewSerializer().delete(request.data)
        elif request.method == 'GET':
                return ViewRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def view_list(request):
        return ViewRepository().get_all()


