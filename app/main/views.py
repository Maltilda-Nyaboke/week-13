from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db
from flask_login import login_required,current_user
from ..models import User



@main.route('/')
def index():
    return render_template('index.html',user= current_user)

@main.route('/new_blog <id>',methods=['POST', 'GET']) 
@login_required
def new_blog(id): 
    return render_template('new_blog.html') 


  