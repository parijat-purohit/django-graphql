# Django GraphQL Project
This project demonstrates how to implement a GraphQL API using Django with two models: `Book` and `FavoriteBook`. It showcases how GraphQL can outperform traditional REST APIs in certain scenarios.

### Features

- **GraphQL API** to query `Book` and `FavoriteBook` models.
- Filter books by whether they are recommended or not.
- Fetch detailed information about books along with their ratings and recommendations.

## Models
### Book

This mode represents a book and includes the following fields.
- `name`: The name of the book (string). 
- `author_name`: The author of the book (string).

```python
class Book(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
```

### FavoriteBook

This model represents a user's favorite book along with a rating and recommendation status.
- `book`: A OneToOne field to the `Book` model.
- `rating`: A numerical rating for the book (0<=rating<=10).
- `recommend_to_read`: A boolean flag indicating whether the book is recommended.

```python
class FavoriteBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    recommend_to_read = models.BooleanField(default=True)
```

### GraphQL Schema

The GraphQL schema exposes the following queries:
- `allBooks`: Fetch all books.
- `bookByRec: Fetch books filtered by their recommendation status.

```python
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book_by_rec = graphene.List(FavoriteBookType, rec=graphene.Boolean(required=True))

    def resolve_all_books(self, info):
        return Book.objects.all()

    def resolve_book_by_rec(self, info, rec):
        return FavoriteBook.objects.filter(recommend_to_read=rec)
```

### Simple Setup Demonstration![Alt text]

For this demonstration, we used a simple setup incorporating a `Dockerfile` and `docker-compose`. The GraphQL setup was based on the guidelines provided in the [Graphene documentation](https://docs.graphene-python.org/en/latest/).

On our localhost, we made our query in following GraphQL endpoint.
```python
http://localhost:8000/graphql/
```
### Testing the Queries

Screen Shot 2024-11-22 at 12.14.29 AM.png






