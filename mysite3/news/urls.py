#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/25 11:29
# Author  : dongchao
# File    : urls.py
# Software: PyCharm


from django.urls import path

from . import views

urlpatterns = [
    # index
    path('index', views.index_view, name="news_url")
]
