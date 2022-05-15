from flask import Blueprint
from flask import render_template
from . import auth
from . import views,forms


auth = Blueprint('auth',__name__)



@auth.route('/login')
def login():
    return render_template('auth/login.html')


