from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('书名', max_length=50, default="")
    pub = models.CharField('出版社', max_length=150, default='')
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=7, decimal_places=2, default=0.0)
    is_activate = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = "book"
        verbose_name = "图书类"
        verbose_name_plural = "图书"

    def __str__(self):
        return f"{self.title}_{self.pub}_{self.price}_{self.market_price}"

    def save(self, *args, **kwargs):
        if not self.id:
            last_book = Book.objects.order_by('-id').first()
            self.id = last_book.id + 1 if last_book else 1
        super(Book, self).save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField("姓名", max_length=11)
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("电子邮箱", null=True)

    class Meta:
        db_table = "author"
        verbose_name = "作者类"
        verbose_name_plural = "作者"

    def __str__(self):
        return f"{self.name}_{self.age}_{self.email}"

    def save(self, *args, **kwargs):
        if not self.id:
            last_author = Author.objects.order_by('-id').first()
            self.id = last_author.id + 1 if last_author else 1
        super(Author, self).save(*args, **kwargs)


