from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author}"

