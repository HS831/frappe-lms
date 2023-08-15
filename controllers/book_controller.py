from flask import Flask, request, Blueprint, jsonify
from models.books import book_schema, Book
from models.members import member_schema, Member
from models.issueBook import issue_book_schema, IssuedBook

from database import db
from models.marshmallow import ma


book_bp = Blueprint('book', __name__)

@book_bp.route('/api/books', methods=['GET'])
def get_all_books(): 
   books = Book.query.all() 

   book_list = []
   for book in books:
      book_list.append({
         'book_id': book.book_id,
         'title': book.title,
         'authors': book.authors,
         'average_rating': book.average_rating,
         'isbn': book.isbn,
         'isbn13': book.isbn13,
         'language_code': book.language_code,
         'num_pages': book.num_pages,
         'ratings_count': book.ratings_count,
         'text_reviews-count': book.text_reviews_count,
         'publication_date': book.publication_date,
         'publisher': book.publisher
      })
   return jsonify({"data": book_list})

@book_bp.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
   book = Book.query.get(book_id)
   book_data = {
      'book_id': book.book_id,
      'title': book.title,
      'authors': book.authors,
      'average_rating': book.average_rating,
      'isbn': book.isbn,
      'isbn13': book.isbn13,
      'language_code': book.language_code,
      'num_pages': book.num_pages,
      'ratings_count': book.ratings_count,
      'text_reviews-count': book.text_reviews_count,
      'publication_date': book.publication_date,
      'publisher': book.publisher
   }
   return jsonify({"data": book_data})


@book_bp.route('/api/books', methods=['POST'])
def add_book():
  book_id = request.json['book_id']
  title = request.json['title']
  authors = request.json['authors']
  average_rating = request.json['average_rating']
  isbn = request.json['isbn']
  isbn13 = request.json['isbn13']
  language_code = request.json['language_code']
  num_pages = request.json['num_pages']
  ratings_count = request.json['ratings_count']
  text_reviews_count = request.json['text_reviews_count']
  publication_date = request.json['publication_date']
  publisher = request.json['publisher']


  new_book = Book(book_id, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher)

  db.session.add(new_book)
  db.session.commit()

  return book_schema.jsonify(new_book)


@book_bp.route('/api/books/issueBook', methods=['POST'])
def issue_book():
  issue_id = request.json['issue_id']
  book_id = request.json['book_id']
  member_id = request.json['member_id']
  issue_date = request.json['issue_date']
  return_date = None
  rent_fee = None

  book = Book.query.get(book_id)

  if not book:
     return jsonify({"message": "No such book present in Library!"})
     

  member = Member.query.get(member_id)

  if member :
     if member.outstanding_debt < 500:
        new_issue_book = IssuedBook(issue_id, book_id, member_id, issue_date, return_date, rent_fee)
        db.session.add(new_issue_book)
        db.session.commit()
        return issue_book_schema.jsonify(new_issue_book)
     else :
        return jsonify({"message": "Your outstanding debt amuount is more than 500! You cannot issue a book!"})
     
  else:
     return jsonify({"message": "No such member found"})
  
@book_bp.route('/api/books/issueBook', methods = ['GET'])
def get_all_issued_books():
   issued_books = IssuedBook.query.all()

   issuedBookList = []
   for issued_book in issued_books:
    issuedBookList.append({
      'issue_id': issued_book.issue_id,
      'book_id': issued_book.book_id,
      'member_id': issued_book.member_id,
      'issue_date': issued_book.issue_date,
      'return_date': issued_book.return_date,
      'rent_fee': issued_book.rent_fee
    })

   return jsonify({"data": issuedBookList})
  
  
@book_bp.route('/api/books/issueReturn', methods=['POST'])
def issue_return():
  issue_id = request.json['issue_id']
  return_date = request.json['return_date']

  issued_book = IssuedBook.query.get(issue_id)

  if issued_book:
    rent_fee = 50
    issued_book.return_date = return_date
    issued_book.rent_fee = rent_fee
    db.session.commit()

    member = Member.query.get(issued_book.member_id)
    member.outstanding_debt += rent_fee
    db.session.commit()

    if(member.outstanding_debt <= 500):
       return jsonify({"message": "Book returned successfully!"})
    else:
       db.session.rollback()
       return jsonify({"error": "Outstanding debt exceeds Rs. 500. Pay your full debt amount!"})
    
  else: 
     return jsonify({"message": "Issue id not found!"}), 404