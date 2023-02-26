from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .productScript import GetSuggestion
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
@csrf_exempt
def ping(request):
    return Response("OK", status=status.HTTP_200_OK)
    
@api_view(['GET'])
@csrf_exempt
def getRandomProduct(request):
    product             = GetSuggestion()
    return Response(
        data        = product, 
        status      = status.HTTP_200_OK
    )
    