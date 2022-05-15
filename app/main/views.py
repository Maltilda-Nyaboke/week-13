from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db
from flask_login import login_required,current_user
from ..models import User



@main.route('/')
@login_required
def index():
    return render_template('index.html',user= current_user)

@main.route('/new_blog <id>',methods=['POST', 'GET']) 
@login_required
def new_blog(id): 
    if request.method == 'POST':
        text=request.form.get('text')
    return render_template('blog.html',user= current_user) 


  