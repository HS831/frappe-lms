from database import db
from models.marshmallow import ma

class Member(db.Model):
    member_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    outstanding_debt = db.Column(db.Float, default=0.0)

    def __init__(self, member_id, name, email, outstanding_debt):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.outstanding_debt = outstanding_debt

# Member Schema
class MemberSchema(ma.Schema):
  class Meta:
    fields = ('member_id', 'name', 'email', 'outstanding_debt')

# Init schema
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)