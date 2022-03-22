from django.db import models
from book.models import Book
from reader.models import Reader


# Create your models here.

class Borrow(models.Model):
    date_borrow = models.DateField()
    expired_date_borrow = models.DateField()
    return_date_borrow = models.DateField()
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_by = models.IntegerField(default=1)
    modified_by = models.IntegerField(default=1)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return '{} {} {} {}'.format(
            self.pk,
            self.book.title_book,
            self.reader.first_name_reader,
            self.expired_date_borrow
        )
