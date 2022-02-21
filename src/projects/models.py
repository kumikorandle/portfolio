from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.TextField()
    repo = models.URLField()
    link = models.URLField(blank=True, default='')

class Image(models.Model):
    description = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/screenshots')