from django.contrib import admin

# Register your models here.
from otm.models import Publisher,Book


class PublisherManager(admin.ModelAdmin):
    list_display = ["name"]


class BookManager(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Publisher, PublisherManager)
admin.site.register(Book, BookManager)
