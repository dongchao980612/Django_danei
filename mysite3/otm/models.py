from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField("出版社名称", max_length=11)
    # 反向属性 wife

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "author_in_otm"
        verbose_name = "出版社类"
        verbose_name_plural = "出版社"


class Book(models.Model):
    title = models.CharField("书名", max_length=11)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "book_in_otm"
        verbose_name = "图书类"
        verbose_name_plural = "图书"
