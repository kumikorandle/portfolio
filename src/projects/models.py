from distutils.command.upload import upload
from django.db import models
from technology.models import Technology

import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.TextField(help_text='Describe your role in the project (e.g., front end developer)')
    repo = models.URLField()
    link = models.URLField(blank=True, default='')
    date = models.DateField(default=datetime.date.today,help_text="Enter the date the project was completed.")
    technology = models.ManyToManyField(Technology, blank=True)

    def __str__(self):
        """String representation of the Project object"""
        return self.title

    def display_technologies(self):
        """Create a string for technologies. Required to display string in Admin."""
        return ', '.join([technology.name for technology in self.technology.all()])

    display_technologies.short_description = "Technologies"

class Image(models.Model):
    description = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/screenshots')