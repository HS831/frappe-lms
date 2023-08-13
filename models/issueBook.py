from database import db
from models.marshmallow import ma

class IssuedBook(db.Model):
    issue_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'))
    issue_date = db.Column(db.String(255))
    return_date = db.Column(db.String(255))
    rent_fee = db.Column(db.Float)

    def __init__(self, issue_id, book_id, member_id, issue_date, return_date, rent_fee):
        self.issue_id = issue_id
        self.book_id = book_id
        self.member_id = member_id
        self.issue_date = issue_date
        self.return_date = return_date
        self.rent_fee = rent_fee

# Issue Schema
class IssueBookSchema(ma.Schema):
  class Meta:
    fields = ('issue_id', 'book_id', 'member_id', 'issue_date', 'return_date', 'rent_fee')

# Init schema
issue_book_schema = IssueBookSchema()
issue_books_schema = IssueBookSchema(many=True)