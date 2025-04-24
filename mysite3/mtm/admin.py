from django.contrib import admin

# Register your models here.
from mtm.models import Author, Book


class AuthorManager(admin.ModelAdmin):
    list_display = ["name"]


class BookManager(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Author, AuthorManager)
admin.site.register(Book, BookManager)
