from django.contrib import admin
from .models import Technology

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

# Register your models here.
admin.site.register(Technology, TechnologyAdmin)