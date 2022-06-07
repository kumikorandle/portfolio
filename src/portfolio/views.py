from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from projects.models import Project
from projects.serializers import *

from technology.models import Technology
from technology.serializers import *

@api_view(["GET"])
def home(request):
    # Retrieve all projects and technologies used
    project_data = Project.objects.all()
    tech_data = Technology.objects.all()

    tech_serializer = TechnologySerializer(tech_data, context={'request': request}, many=True)
    project_serializer = ProjectsSerializer(project_data, context={'request': request}, many=True)

    context = {
        "title":"Kumiko Randle's Portfolio",
        "projects": project_serializer.data,
        "technologies": tech_serializer.data,
    }

    return Response(context)
