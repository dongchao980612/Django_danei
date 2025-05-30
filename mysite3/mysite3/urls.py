"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_static/', views.test_static),
    path("", views.index),
    path("index/", views.index),
    # music
    path('music/', include("music.urls")),
    path('news/', include("news.urls")),
    path('sport/', include("sport.urls")),
    path('bookstore/', include("bookstore.urls")),



    path('set_cookies/', views.set_cookies),
    path('get_cookies/', views.get_cookies),
    path('get_sessions/', views.get_sessions),
    path('set_sessions/', views.set_sessions),
]
