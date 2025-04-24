#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/25 10:56
# Author  : dongchao
# File    : views.py
# Software: PyCharm
from django.shortcuts import render, HttpResponse


def test_static(request):
    return render(request, "test_static.html")


def index(request):
    return render(request, "index.html")


def set_cookies(request):
    resp = HttpResponse("set cookies is ok")
    resp.set_cookie("uuid", "dongchao", 600)
    return resp


def set_sessions(request):
    request.session['uname'] = "dongchao"
    return HttpResponse("set sessions ok")


def get_sessions(request):
    uname = request.session.get("uname")
    return HttpResponse(f"uname = {uname}")


def get_cookies(request):
    uuid = request.COOKIES.get("uuid")
    return HttpResponse(f"cookies = {uuid}")
