from database import db
from models.marshmallow import ma

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    authors = db.Column(db.String(255))
    average_rating = db.Column(db.Float)
    isbn = db.Column(db.String(20))
    isbn13 = db.Column(db.String(20))
    language_code = db.Column(db.String(10))
    num_pages = db.Column(db.Integer)
    ratings_count = db.Column(db.Integer)
    text_reviews_count = db.Column(db.Integer)
    publication_date = db.Column(db.String(20))
    publisher = db.Column(db.String(255))

    def __init__(self, book_id, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.average_rating = average_rating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count
        self.publication_date = publication_date
        self.publisher = publisher

# Book Schema
class BookSchema(ma.Schema):
  class Meta:
    fields = ('book_id', 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages', 'ratings_count', 'text_reviews_count', 'publication_date', 'publisher')

# Init schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)