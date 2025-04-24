from django.contrib import admin

# Register your models here.
from .models import User


class UserManager(admin.ModelAdmin):
    # 列表显示那些字段的列
    list_display = ["username", "password", 'created_time', "updated_time"]
    # 哪些可以链接进入修改页面
    # list_display_links = ["username"]
    # # 过滤器
    # list_filter = ["username"]
    # # 支持搜索的字段【模糊查询】
    # search_fields = ["username"]
    # # 可编辑字段
    # list_editable = ["username"]



admin.site.register(User, UserManager)
