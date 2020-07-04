"""CRUD_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App_FBV_API/', include('App_FBV_API.urls')),
    path('App_CBV_API/', include('App_CBV_API.urls')),
    path('App_Generic_CBV_API/', include('App_Generic_CBV_API.urls')),
    path('App_ViewSet_API/', include('App_ViewSet_API.urls')),
    path('App_Generic_ViewSet_API/', include('App_Generic_ViewSet_API.urls')),
]
