from django.contrib import admin
from myfavbooks.models import Book, FavoriteBook

admin.site.register(Book)
admin.site.register(FavoriteBook)
