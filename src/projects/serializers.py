from rest_framework import serializers
from .models import Project

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project 
        fields = ('pk','title','description','role','repo','link','date','technology')