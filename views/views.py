from flask import Blueprint, render_template

view_index = Blueprint('view_index', __name__, template_folder='templates',url_prefix='/')

@view_index.route('/', methods=['GET'])
def index():
    return render_template('index.html')