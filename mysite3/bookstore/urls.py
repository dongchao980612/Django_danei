#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/25 20:25
# Author  : dongchao
# File    : urls.py
# Software: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    # index
    path('all_book/', views.index_view),
    path('update_book/<int:book_id>/', views.update_view),
    path('delete_book/<int:book_id>/', views.delete_view),
    path('add_book/', views.add_view),

]
