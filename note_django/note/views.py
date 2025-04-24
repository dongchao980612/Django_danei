from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.
from note.models import Note
from user.models import User


def check_login(fn):
    def warp(request, *args, **kwargs):
        if "username" not in request.session or "uid" not in request.session:
            c_uid = request.session.get("uid")
            c_username = request.session.get("username")
            if not c_uid or not c_username:
                return HttpResponseRedirect("/user/login")
            else:
                request.session["uid"] = c_uid
                request.session["username"] = c_username

        return fn(request, *args, **kwargs)

    return warp


@check_login
def list_view(request):
    # all_notes = Note.objects.all()
    all_notes = Note.objects.filter(is_activate=True)
    return render(request, "note/list_note.html", locals())


@check_login
def update_view(request, note_id):
    # 1、查
    try:
        note = Note.objects.get(id=note_id, is_activate=True)
    except Exception as e:
        return HttpResponse(e)

    if request.method == "GET":
        return render(request, "note/update_note.html", locals())
    elif request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        # 2、改
        note.title = title
        note.content = content

        # 3、存
        note.save()
        return HttpResponseRedirect("/note/list_note")


def delete_view(request, note_id):
    # 1、查
    try:
        note = Note.objects.get(id=note_id, is_activate=True)
        note.is_activate = False
        note.save()
        # book.delete()
        return HttpResponseRedirect("/note/list_note")
    except Exception as e:
        return HttpResponse(e)


@check_login
def add_view(request):
    if request.method == "GET":
        return render(request, "note/add_note.html", locals())
    elif request.method == "POST":

        title = request.POST["title"]
        content = request.POST["content"]
        uid = request.session["uid"]

        note = Note()
        note.user_id = uid
        note.title = title
        note.content = content

        note.save()
        return HttpResponseRedirect("/note/list_note")
