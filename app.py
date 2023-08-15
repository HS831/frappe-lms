from flask import Flask
from dotenv import load_dotenv
from database import db
from models.marshmallow import ma
from urllib.parse import quote

from controllers.book_controller import book_bp
from controllers.member_controller import member_bp
from controllers.data_import_controller import data_import

from views.view_book import view_book_bp
from views.views import view_index
from views.view_member import view_member_bp

import os

app = Flask(__name__)

load_dotenv()

# Configure the SQLAlchemy databases
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:%s@localhost:3306/frappe_db' %quote('harshitmishra831@')
DATABASE_URL = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

try:
    with app.app_context():
        db.engine.connect()
        db.create_all()
    print("Database connected successfully!")
except Exception as e:
    print("Database connection failed:", str(e))
   

# Import and register the blueprints here
app.register_blueprint(book_bp)
app.register_blueprint(member_bp)
app.register_blueprint(data_import)

app.register_blueprint(view_index)
app.register_blueprint(view_book_bp)
app.register_blueprint(view_member_bp)

if __name__ == '__main__':
    app.run(debug=True)


