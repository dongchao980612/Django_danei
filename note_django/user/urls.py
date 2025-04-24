#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/26 19:49
# Author  : dongchao
# File    : urls.py
# Software: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('reg/', views.reg_view,name='reg'),
    path('login/', views.login_view, name='login'),
    path('login_out/', views.login_out_view, name='logout'),

]
