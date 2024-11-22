import graphene
from graphene_django import DjangoObjectType

from myfavbooks.models import Book, FavoriteBook


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("name", "author_name")


class FavoriteBookType(DjangoObjectType):
    class Meta:
        model = FavoriteBook
        fields = ("book", "rating", "recommend_to_read")


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book_by_rec = graphene.List(
        FavoriteBookType, rec=graphene.Boolean(required=True))

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_book_by_rec(self, info, rec):
        return FavoriteBook.objects.filter(recommend_to_read=rec)


schema = graphene.Schema(query=Query)
