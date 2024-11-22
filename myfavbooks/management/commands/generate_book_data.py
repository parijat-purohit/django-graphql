from django.core.management.base import BaseCommand
from myfavbooks.models import Book, FavoriteBook

import logging

log = logging.getLogger(__name__)
log.info("Hello")


class Command(BaseCommand):
    help = "Generate sample Book and FavoriteBook objects if they don't already exist"

    def handle(self, *args, **kwargs):
        log.info("Script Started")
        # Define sample data
        book_data = [
            {"name": "Animal Farm", "author_name": "George Orwell"},
            {"name": "1984", "author_name": "George Orwell"},
            {"name": "The Psychology of Money", "author_name": "Morgan Housel"},
            {"name": "Rich Dad Poor Dad", "author_name": "Robert Kiyosaki"},
            {"name": "The Alchemist", "author_name": "Paulo Coelho"},
            {"name": "The Wealth Money Can't Buy", "author_name": "Robin Sharma"},
            {"name": "Fight Club", "author_name": "Chuck Palahniuk"},
            {"name": "Origin", "author_name": "Dan Brown"},
            {"name": "Ikigai", "author_name": "Héctor García"},
            {"name": "Tintorettor Jishu", "author_name": "Satyajit Roy"}
        ]
        favorite_book_data = [
            {"book_name": "Animal Farm", "rating": 10, "recommend_to_read": True},

            {"book_name": "1984", "rating": 9, "recommend_to_read": True},

            {"book_name": "The Psychology of Money",
                "rating": 9, "recommend_to_read": True},

            {"book_name": "Rich Dad Poor Dad",
                "rating": 9, "recommend_to_read": True},

            {"book_name": "The Alchemist", "rating": 9, "recommend_to_read": True},

            {"book_name": "The Wealth Money Can't Buy",
                "rating": 7, "recommend_to_read": False},

            {"book_name": "Fight Club", "rating": 8, "recommend_to_read": True},
            {"book_name": "Origin", "rating": 9, "recommend_to_read": True},
            {"book_name": "Ikigai", "rating": 8, "recommend_to_read": True},
            {"book_name": "Tintorettor Jishu",
                "rating": 10, "recommend_to_read": True}
        ]

        # Create Book objects if they don't exist
        for data in book_data:
            book, created = Book.objects.get_or_create(
                name=data["name"], author_name=data["author_name"])
            if created:
                log.info(f"Created Book: {book.name}")

        # Create FavoriteBook objects if they don't exist
        for data in favorite_book_data:
            try:
                book = Book.objects.get(name=data["book_name"])
                _, created = FavoriteBook.objects.get_or_create(
                    book=book,
                    defaults={
                        "rating": data["rating"],
                        "recommend_to_read": data["recommend_to_read"],
                    },
                )
                if created:
                    log.info(f"Created FavoriteBook for: {book.name}")
            except Book.DoesNotExist:
                log.warning(f"Book {data['book_name']} not found.")

        log.info('Done.')
