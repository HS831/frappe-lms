from database import db
from models.marshmallow import ma

class Transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'))
    transaction_type = db.Column(db.String(20))
    transaction_date = db.Column(db.DateTime)
    amount = db.Column(db.Float)

    def __init__(self, transaction_id, member_id, transaction_type, transaction_date, amount):
       self.transaction_id = transaction_id
       self.member_id = member_id
       self.transaction_type = transaction_type
       self.transaction_date = transaction_date
       self.amount = amount

# Transaction Schema
class TransactionSchema(ma.Schema):
  class Meta:
    fields = ('transaction_id', 'member_id', 'transaction_type', 'transaction_date', 'amount')

# Init schema
transaction_schema = TransactionSchema()
transactions_schema =TransactionSchema(many=True)