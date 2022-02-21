from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Technology(models.Model):
    TYPE = [
        ('WD', 'Website Development'),
        ('IDE', 'Integrated Development Environment'),
        ('GD', 'Graphic Design'),
        ('PL', 'Programming Language')
    ]

    type = models.CharField(max_length=100, choices=TYPE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/technology')