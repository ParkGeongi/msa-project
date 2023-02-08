from django.http import JsonResponse, QueryDict
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from ml.mnist.fashion_service import FashionService


