from django.shortcuts import render
from django.http import *

# Create your views here.
from bookstore.models import Book


def index_view(request):
    # all_books = Book.objects.all()
    all_books = Book.objects.filter(is_activate=True)
    return render(request, "bookstore/all_books.html", locals())


def update_view(request, book_id):
    # 1、查
    try:
        book = Book.objects.get(id=book_id,is_activate=True)
    except Exception as e:
        return HttpResponse(e)

    if request.method == "GET":
        return render(request, "bookstore/update_book.html", locals())
    elif request.method == "POST":
        req_price = request.POST["price"]
        req_market_price = request.POST["market_price"]

        # 2、改
        book.price = req_price
        book.market_price = req_market_price

        # 3、存
        book.save()
        return HttpResponseRedirect("/bookstore/all_book")


def delete_view(request, book_id):
    # 1、查
    try:
        book = Book.objects.get(id=book_id,is_activate=True)
        book.is_activate = False
        book.save()
        # book.delete()
        return HttpResponseRedirect("/bookstore/all_book")
    except Exception as e:
        return HttpResponse(e)


def add_view(request):
    if request.method == "GET":
        return render(request, "bookstore/add_book.html", locals())
    elif request.method == "POST":
        req_title = request.POST["title"]
        req_pub = request.POST["pub"]
        req_price = request.POST["price"]
        req_market_price = request.POST["market_price"]

        book = Book()
        book.title = req_title
        book.pub = req_pub
        book.price = req_price
        book.market_price = req_market_price
        book.save()
        return HttpResponseRedirect("/bookstore/all_book")
