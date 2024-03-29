"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from projects import views as project_views
from technology import views as tech_views
from .views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', home, name='index'),
    path('projects/', project_views.projects, name='projects'),
    path('technologies/', tech_views.technologies, name="technologies"),
    path('projects/<int:pk>/', project_views.project_detail, name='project_detail'),
    path('search/<int:pk>', project_views.project_search, name='project_search'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)