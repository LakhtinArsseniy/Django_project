from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)