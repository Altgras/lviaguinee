from django.db import models
from book.models import ReadPoint


# Create your models here.
class Reader(models.Model):
    gender = [
        ("f", "feminin"),
        ('m', 'masculin')
    ]

    first_name_reader = models.CharField(max_length=20)
    last_name_reader = models.CharField(max_length=20)
    nationality_reader = models.CharField(max_length=20)
    phone1_reader = models.CharField(max_length=20)
    phone2_reader = models.CharField(max_length=20)
    email_reader = models.CharField(max_length=20)
    gender_reader = models.CharField(max_length=1,choices=gender)
    address_reader = models.CharField(max_length=30)
    # image_reader = models.ImageField(upload_to='/media/image')
    type_piece_reader = models.CharField(max_length=30)
    number_piece_reader = models.CharField(max_length=30)
    # image_piece_reader = models.ImageField(upload_to='/media/image')
    readpoint = models.ForeignKey(ReadPoint,on_delete=models.CASCADE)
    created_by = models.IntegerField(default=1)
    modified_by = models.IntegerField(default=1)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return '{} {} {} {}'.format(
            self.pk,
            self.first_name_reader,
            self.last_name_reader,
            self.readpoint.name

    )

