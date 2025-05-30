from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField('用户名', max_length=30, default="", unique=True)
    password = models.CharField("密码", max_length=32)
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    updated_time = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return f"{self.username}"
