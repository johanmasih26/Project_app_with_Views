"""Project URL Configuration

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
from django.http import HttpResponse
from django.urls import path
from .views import projectView, projectsView, projectCreateView, projectUpdateView, projectDeleteView

from . import views


urlpatterns = [
    path('projects', projectsView.as_view(), name='projects'),
    path('project/<str:pk>', projectView.as_view(), name='project'),
    path('project-create/', projectCreateView.as_view(), name='project_create'),
    path('project-update/<str:pk>', projectUpdateView.as_view(), name='project_update'),
    path('project-delete/<str:pk>', projectDeleteView.as_view(), name='project_delete'),
]
