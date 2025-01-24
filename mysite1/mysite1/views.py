#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/24 14:26
# Author  : dongchao
# File    : views.py
# Software: PyCharm


from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse


def page_2003_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def page_index_view(request):
    html = "<h1>这是首页</h1>"
    return HttpResponse(html)


def page1_view(request):
    html = "<h1>这是编号为1的页面</h1>"
    return HttpResponse(html)


def page2_view(request):
    html = "<h1>这是编号为2的页面</h1>"
    return HttpResponse(html)


def pagen_view(request, page):
    html = f"<h1>这是编号为{page}的页面！</h1>"
    return HttpResponse(html)


def cal_view(request, m, op, n):
    if op not in ["add", "sub", "mul", "div"]:
        return HttpResponse("<h1>You op is wrong!</h1>")
    result = None
    m = int(m)
    n = int(n)
    if op == "add":
        result = m + n
    elif op == "sub":
        result = m - n
    elif op == "mul":
        result = m * n
    elif op == "div":
        try:
            result = m / n
        except ZeroDivisionError as e:
            return HttpResponse(f"<h1>{e}</h1>")

    html = f"<h1>结果是：{result}</h1>"
    return HttpResponse(html)


def cal2_view(request, m, op, n):
    if op not in ["add", "sub", "mul", "div"]:
        return HttpResponse("<h1>You op is wrong!</h1>")
    m = int(m)
    n = int(n)
    result = None
    if op == "add":
        result = m + n
    elif op == "sub":
        result = m - n
    elif op == "mul":
        result = m * n
    elif op == "div":
        try:
            result = m / n
        except ZeroDivisionError as e:
            return HttpResponse(f"<h1>{e}</h1>")

    html = f"<h1>结果是：{result}!</h1>"
    return HttpResponse(html)


def cal_bitrhday_view(request, y, m, d):
    return HttpResponse(f"<h1>{y}年{m}月{d}日</h1>")


def test_request(request):
    print(f"path info = {request.path_info}")
    print(f"get_full_path_info = {request.get_full_path_info()}")
    print(f"method = {request.method}")
    print(f"querystring = {request.GET}")
    print(f"REMOTE_ADDR = {request.META['REMOTE_ADDR']}")

    return HttpResponseRedirect("/")
    # return HttpResponse("<h1>Test ok!</h1>")


POST_FORM = """
<form method='post' action"/test_get_post'>
    用户名：<input type='text' name='username'>
    <input type='submit' value='提交'>
</form>
"""


def test_get_post(request):
    if request.method == "GET":
        # print(request.GET["a"])
        # print(request.GET.get("a"))
        # print(request.GET.getlist("a"))
        # print(request.GET.get("b", "no b"))
        return HttpResponse(POST_FORM)
    elif request.method == "POST":
        print(request.POST.get("username"))
        return HttpResponse("<h1>post is ok!</h1>")
    else:
        pass
    return HttpResponse("<h1>test get ok!</h1>")


def test_html_request(request):
    # 方案1
    # from django.template import loader
    # t = loader.get_template("test_html.html")
    # html = t.render()
    # return HttpResponse(html)
    # 方案2
    dic = {
        "username": "admin",
        "passwd": "root"
    }
    return render(request, 'test_html.html', dic)


def say_hi():
    return "hello world"


class Dog:
    def say(self):
        return "hello dog!"


def test_html_param(request):
    dic = {
        "int": 88,
        "str": "admin",
        "lst": ["Tom", "Timi", "Jack"],
        "dic": {"username": "admin", "passwd": "root"},
        "func": say_hi,
        "class_obj": Dog(),
        "script": "<h1>test html param</h1>"
    }
    return render(request, 'test_html_param.html', dic)


def test_if_for(request):
    dic = {
        "x": 9,
        "str": "admin",
        "lst": ["Tom", "Timi", "Jack"],
    }
    return render(request, 'test_if_for.html', dic)


def test_mycal(request):
    if request.method == "GET":
        print("Get...")
        return render(request, 'mycal.html')
    elif request.method == "POST":
        print("POST...")
        x = request.POST.get("x")
        y = request.POST.get("y")
        op = request.POST.get("op")
        if op not in ["add", "sub", "mul", "div"]:
            return HttpResponse("<h1>You op is wrong!</h1>")
        result = None
        x = int(x)
        y = int(y)
        if op == "add":
            result = x + y
        elif op == "sub":
            result = x - y
        elif op == "mul":
            result = x * y
        elif op == "div":
            try:
                result = x / y
            except ZeroDivisionError as e:
                return HttpResponse(f"<h1>{e}</h1>")
        dic = {
            "x": x, "y": y, "result": result, "op": op
        }
        return render(request, 'mycal.html', dic)
    return HttpResponse("")


def base_view(request):
    return render(request, 'base.html')


def base_view(request):
    return render(request, 'base.html')


def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')


def test_url(request):
    return render(request, 'test_url.html')


def test_url_result(request, page):
    url = reverse("base")
    return HttpResponseRedirect(url)
    # return HttpResponse(f"test_url OK {page}")
