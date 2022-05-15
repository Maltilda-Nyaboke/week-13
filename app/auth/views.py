from flask import render_template,redirect, url_for,flash,request
from flask_login import login_user,logout_user,login_required
from .. import db
from .import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    return render_template('auth/login.html')  



@auth.route('/register',methods = ['GET','POST'])
def register():
    email = request.form.get('email')
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    return render_template('auth/register.html')

@auth.route('/')
def logout():
    logout_user()
    return render_template('main.index')
