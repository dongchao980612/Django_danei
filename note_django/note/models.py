from django.db import models

# Create your models here.
from user.models import User


class Note(models.Model):
    title = models.CharField("标题", max_length=100)
    content = models.TextField("内容")
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    updated_time = models.DateTimeField("更新时间", auto_now=True)
    is_activate = models.BooleanField('是否活跃', default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Note"
        verbose_name = "笔记"
        verbose_name_plural = "笔记"

    def __str__(self):
        return f"{self.title}"

