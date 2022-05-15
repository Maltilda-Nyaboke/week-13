from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/new_blog <id>',methods=['POST', 'GET']) 
@login_required
def new_blog(id): 
    return render_template('new_blog.html')  