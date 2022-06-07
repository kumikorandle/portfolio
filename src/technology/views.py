from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from technology.models import Technology
from .serializers import *

# Create your views here.
@api_view(["GET"])
def technologies(request):
    data = Technology.objects.all()

    serializer = TechnologySerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)