"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Man.views
import Women.views
import login.views
import Main.views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('Man', Man.views.Manhome, name='Manhome'),
    path('Man1', Man.views.man1, name='man1'),
    path('Man2', Man.views.man2, name='man2'),
    path('Man3', Man.views.man3, name='man3'),
    path('Man4', Man.views.man4, name='man4'),
    path('Man5', Man.views.man5, name='man5'),
    path('Man6', Man.views.man6, name='man6'),
    path('Man7', Man.views.man7, name='man7'),
    path('Man8', Man.views.man8, name='man8'),
    path('Women', Women.views.Womenhome, name='Womenhome'),
    path('Women1', Women.views.women1, name='women1'),
    path('Women2', Women.views.women2, name='women2'),
    path('Women3', Women.views.women3, name='women3'),
    path('Women4', Women.views.women4, name='women4'),
    path('Women5', Women.views.women5, name='women5'),
    path('Women6', Women.views.women6, name='women6'),
    path('Women7', Women.views.women7, name='women7'),
    path('Women8', Women.views.women8, name='women8'),
    path('login/', include('login.urls')),
    path('Main/', include('Main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
