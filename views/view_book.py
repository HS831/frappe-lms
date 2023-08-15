from flask import Flask, request, Blueprint, render_template, jsonify
from dotenv import load_dotenv
from models.books import book_schema, Book

from database import db
from models.marshmallow import ma

import requests
import os

load_dotenv()
view_book_bp = Blueprint('view_book_bp', __name__, template_folder='templates', url_prefix='/books')

@view_book_bp.route('/', methods=['GET'])
def get_books():
    protocol = request.scheme
    hostname = request.host.split(':')[0]
    
    print(os.getenv('ENV'))

    if(os.getenv('ENV') == "DEV"):
        port = request.host.split(':')[1]
        api_url = f"{protocol}://{hostname}:{port}/api/books"
    else:
        api_url = f"{protocol}://{hostname}/api/books"
        

    try:
        response = requests.get(api_url)
        books_data = response.json().get('data', [])
        
        return render_template('books_display.html', books=books_data)
    except Exception as e:
        return str(e)
    
@view_book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    protocol = request.scheme
    hostname = request.host.split(':')[0]

    if(os.getenv('ENV') != 'DEV'):
        port = request.host.split(':')[1]
        api_url = f"{protocol}://{hostname}:{port}/api/books{book_id}"
    else:
        api_url = f"{protocol}://{hostname}/api/books{book_id}"

    try:
        response = requests.get(api_url)
        book_data = response.json().get('data', [])
        
        return render_template('book_display.html', book=book_data)
    except Exception as e:
        return str(e)
    
@view_book_bp.route('/issue', methods=['GET'])
def issue_book_render():
    return render_template('issue_book.html')

@view_book_bp.route('/issue/view', methods=['GET'])
def view_issued_books():
    protocol = request.scheme
    hostname = request.host.split(':')[0]
    
    if(os.getenv('ENV') != 'DEV'):
        port = request.host.split(':')[1]
        api_url = f"{protocol}://{hostname}:{port}/api/issueBook"
    else:
        api_url = f"{protocol}://{hostname}/api/issueBook"

    try:
        response = requests.get(api_url)
        issue_books_data = response.json().get('data', [])
        
        return render_template('view_issued_book.html', issued_books=issue_books_data)
    except Exception as e:
        return str(e)

@view_book_bp.route('/return', methods=['GET'])
def return_book():
    return render_template('return_book.html')






    