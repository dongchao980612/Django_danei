from django.contrib import admin

# Register your models here.
from .models import Book, Author


class BookManager(admin.ModelAdmin):
    # 列表显示那些字段的列
    list_display = ["id", "title", 'price', "market_price"]
    # 哪些可以链接进入修改页面
    list_display_links = ["title"]
    # 过滤器
    list_filter = ["pub"]
    # 支持搜索的字段【模糊查询】
    search_fields = ["title", "pub"]
    # 可编辑字段
    list_editable = ["price", "market_price"]

    ordering = ["id"]
    list_per_page = 10


class AuthorManager(admin.ModelAdmin):
    list_display = ["name", "age", 'email']
    list_display_links = ["name"]
    list_filter = ["age"]
    search_fields = ["name", 'email']
    list_editable = ["age", "email"]
    ordering = ["name"]
    list_per_page = 10


admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
