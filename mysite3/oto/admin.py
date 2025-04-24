from django.contrib import admin

# Register your models here.
from oto.models import Author, Wife


class AuthorManager(admin.ModelAdmin):
    list_display = ["name"]


class WifeManager(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Author, AuthorManager)
admin.site.register(Wife, WifeManager)
