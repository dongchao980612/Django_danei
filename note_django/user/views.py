import hashlib

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render

from user.models import User


def reg_view(request):
    if request.method == "GET":
        return render(request, "user/register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]

        # 判断密码是否李可用
        if password_1 != password_2:
            return render(request, "user/register.html", {"password_msg": "密码不一致"})

        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
        # 判断用户名是否可用
        existd_users = User.objects.filter(username=username)
        if existd_users:
            return render(request, "user/register.html", {"username_msg": "用户名已存在"})
        # 插入数据
        try:
            u = User()
            u.username = username
            u.password = password_m

            request.session["username"] = username
            request.session["uid"] = u.id

            # TODO 修改存储时间为1天
            u.save()

            return HttpResponseRedirect("/index")
        except Exception as e:
            return render(request, "user/register.html", {"username_msg": "用户名已存在"})


def login_view(request):
    if request.method == "GET":
        if request.session.get("username") and request.session.get("uid"):
            return HttpResponseRedirect("/note/list_note")

        c_username = request.COOKIES.get("username")
        c_uid = request.COOKIES.get("uid")
        if c_username and c_uid:
            request.session["username"] = c_username
            request.session["uid"] = c_uid
            return HttpResponseRedirect("/note/list_note")
        return render(request, "user/login.html")

    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # 判断用户名是否可用
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return render(request, "user/login.html", {"error_msg": "用户名或密码错误"})

        m = hashlib.md5()
        m.update(password.encode())

        if m.hexdigest() != user.password:
            return render(request, "user/login.html", {"error_msg": "用户名或密码错误"})

        # 记录会话
        request.session["username"] = username
        request.session["uid"] = user.id

        resp = HttpResponseRedirect("/note/list_note")
        if "remember_username" in request.POST:
            resp.set_cookie("username", username, 3600 * 24 * 3)
            resp.set_cookie("uid", user.id, 3600 * 24 * 3)

        return resp


def login_out_view(request):
    if "username" in request.session:
        del request.session['username']
    if "uid" in request.session:
        del request.session['uid']
    resp = HttpResponseRedirect("/note/list_note")
    if "username" in request.COOKIES:
        resp.delete_cookie("username")
    if "uid" in request.COOKIES:
        resp.delete_cookie("uid")

    return resp
