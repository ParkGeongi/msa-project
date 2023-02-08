from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from movie.theaters_tickets.models import Theater_ticket
from movie.theaters_tickets.serializers import Theater_ticketSerializer


class Theater_TicketRepository(object):

    def __init__(self):
        print(" CommentsRepository 객체 생성 ")

    def get_all(self):
        return Response(Theater_ticketSerializer(Theater_ticket.objects.all(), many=True).data)

    def find_by_id(self,id):
        return Response(Theater_ticketSerializer(Theater_ticket.objects.all(), many=True).data)
