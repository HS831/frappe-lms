from flask import Flask, request, Blueprint, jsonify
from models.members import Member, member_schema

from database import db
from models.marshmallow import ma

member_bp = Blueprint('member', __name__)

@member_bp.route('/api/members', methods=['POST'])
def add_member():
  member_id = request.json['member_id']
  name = request.json['name']
  email = request.json['email']
  outstanding_debt = None


  new_member = Member(member_id, name, email, outstanding_debt)

  db.session.add(new_member)
  db.session.commit()

  return member_schema.jsonify(new_member), 201