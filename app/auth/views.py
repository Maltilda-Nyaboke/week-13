from flask import render_template,redirect, url_for,flash,request
from flask_login import login_user,logout_user,login_required,current_user
from werkzeug.security import generate_password_hash,check_password_hash

from .. import db
from .import auth
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password,password):
               flash('logged in successfully', category='success') 
               login_user(user,remember=True)
            else:
                flash('password is incorrect', category='error') 
        else:
            flash('Invalid username or Password', category='error')
    return render_template('auth/login.html')  



@auth.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        email_exists= User.query.filter_by(email=email).first()
        username_exists =User.query.filter_by(username=username).first() 
        if email_exists:
            flash('User with this email already exists',category = 'error')
        elif username_exists:
            flash('User with this username already exists',category ='error')
        elif password1 != password2:
            flash('passwords don\'t match',category ='error') 
        else: 
            new_user = User(email=email,username=username,password=password1)   
            db.session.add(new_user)
            db.session.commit()
            logout_user(new_user,remember=True)  
            flash('user has been created') 
            return redirect('main.index')
             
    return render_template('auth/register.html')

@auth.route('/')
@login_required
def logout():
    logout_user()
    return render_template('main.index')
