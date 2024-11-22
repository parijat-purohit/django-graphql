from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Book: {self.name}, Author: {self.author_name}"


class FavoriteBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    recommend_to_read = models.BooleanField(default=True)

    def __str__(self):
        return f"Book: {self.book.name}, rating: {self.rating}"
