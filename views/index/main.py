from flask import Blueprint,render_template

index_main_bp = Blueprint('index_main',__name__)

@index_main_bp.route('/')
def index():
    return render_template('index/index.html')

@index_main_bp.route('/about')
def about():
    return '<h1>about</1>'

