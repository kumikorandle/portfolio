from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from projects.models import Project
from projects.serializers import *

from technology.models import Technology
from technology.serializers import *

def home(request):
    return render(request, "build/index.html")