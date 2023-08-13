from flask import Flask, request, Blueprint, jsonify
from models.books import book_schema, Book

from database import db
from models.marshmallow import ma

import requests

data_import = Blueprint('data_import', __name__)

@data_import.route('/api/fetch-frappe-library/<string:page>', methods=['GET'])
def fetch_api(page):
   api_url = f"https://frappe.io/api/method/frappe-library?page={page}"

   try:
        response = requests.get(api_url)
        books_data = response.json().get('message', [])

        for book_data in books_data:
           new_book = Book(
              book_id = book_data.get('bookID'),
              title = book_data.get('title'),
              authors = book_data.get('authors'),
              average_rating = book_data.get('average_rating'),
              isbn = book_data.get('isbn'),
              isbn13 = book_data.get('isbn13'),
              language_code= book_data.get('language_code'),
              num_pages = book_data.get('  num_pages'),
              ratings_count = book_data.get('ratings_count'),
              text_reviews_count = book_data.get('text_reviews_count'),
              publication_date = book_data.get('publication_date'),
              publisher = book_data.get('publisher')
            ) 
           db.session.add(new_book)

        db.session.commit()           
        return jsonify({"message": "Book added into the database!"})
   
   except Exception as e:
      return jsonify({"error": e}), 400