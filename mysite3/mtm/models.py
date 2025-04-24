from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField("姓名", max_length=11)

    # 反向属性 wife

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "author_in_mtm"
        verbose_name = "作者类"
        verbose_name_plural = "作者"


class Book(models.Model):
    title = models.CharField("书名", max_length=11)
    books = models.ManyToManyField(Author)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "book_in_mtm"
        verbose_name = "图书类"
        verbose_name_plural = "图书"
