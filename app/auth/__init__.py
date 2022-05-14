from flask import Blueprint
from flask import render_template
from . import auth


auth = Blueprint('auth',__name__)

from . import views

@auth.route('/login')
def login():
    return render_template('auth/login.html')


