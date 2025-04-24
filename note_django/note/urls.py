#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/27 16:31
# Author  : dongchao
# File    : urls.py
# Software: PyCharm
from django.urls import path

from . import views

urlpatterns = [
    path('list_note/', views.list_view,name='all'),
    path('update_note/<int:note_id>/', views.update_view),
    path('delete_note/<int:note_id>/', views.delete_view),
    path('add_note/', views.add_view),

]