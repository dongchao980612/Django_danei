#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/25 10:56
# Author  : dongchao
# File    : views.py
# Software: PyCharm
from django.shortcuts import render


def test_static(request):
    return render(request, "test_static.html")


def index(request):
    return render(request, "index.html")
