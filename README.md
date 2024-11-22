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
