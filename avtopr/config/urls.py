"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from config import settings
from .views import *


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('pgapp/',include('pgapp.urls')),

    path('zakas/',ZakazOlishView.as_view(),name='zakaz'),
    path('zakazlar/',ZakazlarView.as_view(),name='zakazlar'),
    path('servis/',ServisView.as_view(),name='servis')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
