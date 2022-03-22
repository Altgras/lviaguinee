from django.db import models


class Author(models.Model):
    first_name_author = models.CharField(max_length=50)
    last_name_author = models.CharField(max_length=50)
    biography_author = models.CharField(max_length=255)
    nationality_author = models.CharField(max_length=50)
    created_by = models.IntegerField(default=1)
    modified_by = models.IntegerField(default=1)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "{pk} {first_name_author} {last_name_author}".format(
            pk = self.pk,
            first_name = self.first_name_author,
            last_name = self.last_name_author
        )
# Table Point de lecture
class ReadPoint(models.Model):
    name_readpoint = models.CharField(max_length=50)
    commune_readpoint = models.CharField(max_length=50)
    quartier_readpoint = models.CharField(max_length=50)
    address_readpoint = models.CharField(max_length=50)
    contact1_readpoint = models.CharField(max_length=50)
    contact2_readpoint = models.CharField(max_length=50)
    email_readpoint = models.EmailField(max_length=50)
    created_by = models.IntegerField(default=1)
    modified_by = models.IntegerField(default=1)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "{pk} {name} {commune} {quartier}".format(
            pk=self.pk,
            name=self.name_readpoint,
            commune = self.commune_readpoint,
            quartier=self.quartier_readpoint
        )

class Rayon(models.Model):
    name_rayon = models.CharField(max_length=50)
    readpoint = models.ForeignKey(ReadPoint, on_delete=models.CASCADE)
    created_by = models.IntegerField(default=1)
    modified_by = models.IntegerField(default=1)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "{pk} {rayon} {readpoint}".format(
            pk=self.pk,
            rayon=self.name_rayon,
            readpoint=self.readpoint.name_readpoint
        )
# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=30)
    rayon = models.ForeignKey(Rayon, on_delete=models.CASCADE)
    created_by = models.IntegerField(default=1)
    modified_by = models.IntegerField(default=1)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "{ } { } {}".format(
            self.pk,
            self.rayon,
            self.name_category
        )

class Book(models.Model):
    isbn_book = models.CharField(max_length=30)
    title_book = models.CharField(max_length=30)
    number_copy_book = models.IntegerField()
    publication_date_book = models.DateField()
    # file_book = models.FileField(upload_to='/media')
    # cover_book = models.ImageField(upload_to='media')
    resume_book = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    edition_house = models.CharField(max_length=30)
    created_by = models.IntegerField(default=1)
    modified_by = models.IntegerField(default=1)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "{} {} {}".format(
            self.title_book,
            self.author.name,
            self.edition_house.name
        )
