from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):

    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.CharField(max_length=100)
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)