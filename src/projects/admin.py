from django.contrib import admin
from .models import Project, Image

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_technologies', 'date')

# # Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image)
