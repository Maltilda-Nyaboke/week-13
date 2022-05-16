from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db
from flask_login import login_required,current_user
from ..models import Blog, User,Comment



@main.route('/')
@login_required
def index():
    blogs = Blog.query.all()
    return render_template('index.html', user= current_user,blogs=blogs)

@main.route('/new_blog',methods=['POST', 'GET']) 
@login_required
def new_blog():
    if request.method == "POST":
        blog = request.form.get('blog')

        if not blog:
            flash('Blog cannot be empty', category='error')
        else:
            blog = Blog(blog=blog, writer=current_user.id)
            db.session.add(blog)
            db.session.commit()
            flash('blog created!', category='success')
            return redirect(url_for('main.index'))

    return render_template('blog.html', user = current_user)

@main.route('/delete_blog/<id>')
@login_required
def delete_blog(id):
    blog=blog.query.filter_by(id=id).first()
    if current_user.id == blog.id:
        db.session.delete(blog)
        db.session.commit()

@main.route('/blogs/<username>')
@login_required
def blogs(username): 
    user = User.query.filter_by(username=username).first()
    blogs= user.blogs

    return render_template('blog_display.html',user= current_user,blogs=blogs,username=username)


@main.route('/create_comment/<blog_id>',methods=['POST'])  
@login_required
def create_comment(blog_id):
    text = request.form.get('text')
    blog = Blog.query.filter_by(id = blog_id)
    if blog:
        comment = Comment(text=text,writer = current_user.id ,blog_id=blog_id) 
        db.session.add(comment)
        db.session.commit() 
    return redirect(url_for('main.index'))

@main.route('/delete_comment/<comment_id>')  
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if comment:
        current_user.id == comment.writer and current_user.id == comment.blog.writer
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('main.index'))  
       

  