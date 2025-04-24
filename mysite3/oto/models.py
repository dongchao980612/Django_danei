from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField("姓名", max_length=11)
    # 反向属性 wife

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "author_in_oto"
        verbose_name = "作者类"
        verbose_name_plural = "作者"


class Wife(models.Model):
    name = models.CharField("姓名", max_length=11)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "wife_in_oto"
        verbose_name = "妻子类"
        verbose_name_plural = "妻子"
