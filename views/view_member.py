from flask import Flask, request, Blueprint, render_template, jsonify
from dotenv import load_dotenv
from models.members import member_schema, Member

from database import db
from models.marshmallow import ma

import requests
import os

load_dotenv()

view_member_bp = Blueprint('view_member_bp', __name__, template_folder='templates', url_prefix='/members')

@view_member_bp.route('/', methods=['GET'])
def add_members():
    return render_template('add_members.html')

@view_member_bp.route('/view', methods=['GET'])
def view_members():
    protocol = request.scheme
    hostname = request.host.split(':')[0]
    
    if(os.getenv('ENV') == "DEV"):
        port = request.host.split(':')[1]
        api_url = f"{protocol}://{hostname}:{port}/api/members"
    else:
        api_url = f"{protocol}://{hostname}/api/members"

    try:
        response = requests.get(api_url)
        members_data = response.json().get('data', [])
        
        return render_template('view_members.html', members=members_data)
    except Exception as e:
        return str(e)