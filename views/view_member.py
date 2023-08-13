from flask import Flask, request, Blueprint, render_template, jsonify
from models.members import member_schema, Member

from database import db
from models.marshmallow import ma

import requests

view_member_bp = Blueprint('view_member_bp', __name__, template_folder='templates', url_prefix='/members')

@view_member_bp.route('/', methods=['GET'])
def add_members():
    return render_template('add_members.html')