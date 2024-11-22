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

Use the GraphiQL interface (available at the `/graphql` endpoint) to test the following queries:

### Fetch all books:

```python
{
  allBooks {
    name
    authorName
  }
}
```

### Sample Response

```python
{
  "data": {
    "allBooks": [
      {
        "name": "1984",
        "authorName": "George Orwell"
      },
      {
        "name": "Animal Farm",
        "authorName": "George Orwell"
      }
    ]
  }
}
```

### Fetch books based on their recommendation status (`recommend_to_read`):


```python
{
  bookByRec(rec: true) {
    book {
      name
      authorName
    }
    rating
    recommendToRead
  }
}
```

### Sample Response

```python
{
  "data": {
    "bookByRec": [
      {
        "book": {
          "name": "1984",
          "authorName": "George Orwell"
        },
        "rating": 10
      }
    ]
  }
}
```

## Why GraphQL?

### 1. Single Endpoint for Multiple Queries
In REST APIs, multiple endpoints are required to fetch related resources (e.g., `/books`, `/favorites`, `/books/{id}`). With GraphQL, you only need a single `/graphql` endpoint to access and manipulate multiple types of data in a single query.

### 2. Reduced Over-fetching and Under-fetching
- **Over-fetching**: In REST, you often get more data than you need because responses are predefined by the endpoint. With GraphQL, you can request only the specific fields you need, reducing unnecessary data transfer.
- **Under-fetching**: In REST, you might need to make multiple requests to fetch related data (e.g., first getting books and then fetching ratings). In GraphQL, you can fetch related data in a single query.

### 3. Client-Specified Queries
In REST APIs, the server defines what data is returned. This leads to rigidity and more API versions. In GraphQL, the client can define the structure of the response, making it highly flexible and adaptable to changing requirements.

## Conclusion

This Django GraphQL project simplifies querying and managing related data with a flexible, single-query model, demonstrating how GraphQL can outperform traditional REST APIs by reducing over-fetching, under-fetching, and the need for multiple endpoints. As the application grows, adding new fields or resources can be done without creating new versions or endpoints, ensuring scalability and efficiency.
