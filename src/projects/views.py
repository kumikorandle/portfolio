from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from projects.models import Project
from technology.views import technologies
from .serializers import *


# Create your views here.
@api_view(["GET"])
def project_search(request, pk):
    # Retrieve all projects which use specified technology
    projects = Project.objects.filter(technology__pk=pk)

    serializer = ProjectsSerializer(projects, context={'request': request}, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectsSerializer(project)
    
    return Response(status=status.HTTP_200_OK, data=serializer.data)
