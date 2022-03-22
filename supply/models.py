from django.db import models
from book.models import Book


# Create your models here.
class Supply(models.Model):
    quantity_add_book = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_by = models.IntegerField(default=1)
    modified_by = models.IntegerField(default=1)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return '{} {}'.format(
            self.pk,
            self.quantity_add_book,
            self.book.title_book
        )
