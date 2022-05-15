from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db
from flask_login import login_required,current_user
from ..models import Blog, User



@main.route('/')
@login_required
def index():
    blogs = Blog.query.all()
    return render_template('index.html',user= current_user,blogs=blogs)

@main.route('/new_blog <id>',methods=['POST', 'GET']) 
@login_required
def new_blog(id): 
    if request.method == 'POST':
        blog=request.form.get('blog')
        blog = Blog(blog=blog,writer=current_user.id)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for(')main.index'))
    return render_template('blog.html',user= current_user) 
@main.route('/delete_blog/<id>')
@login_required
def delete_blog(id):
    blog=blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()

  