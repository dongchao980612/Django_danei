from django.contrib import admin

# Register your models here.
from .models import Note


class NoteManager(admin.ModelAdmin):
    # 列表显示那些字段的列
    list_display = ["id", "title"]


admin.site.register(Note, NoteManager)
