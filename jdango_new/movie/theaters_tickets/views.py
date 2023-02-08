from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from movie.theaters_tickets.repositories import Theater_TicketRepository
from movie.theaters_tickets.serializers import Theater_ticketSerializer


# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def theater_ticket(request):
        if request.method == 'POST':
                return Theater_ticketSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return Theater_ticketSerializer().update(request.data)
        elif request.method == 'DELETE':
                return Theater_ticketSerializer().delete(request.data)
        elif request.method == 'GET':
                return Theater_TicketRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def theater_ticket_list(request):
        return Theater_TicketRepository().get_all()



