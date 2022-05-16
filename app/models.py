from .import db
from . import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False,unique=True)
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='user',passive_deletes= True,lazy = 'dynamic')
    comments = db.relationship('Comment', backref='user',passive_deletes= True,lazy = 'dynamic')


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    blog = db.Column(db.String(255))
    writer = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable=False)
    comments = db.relationship('Comment', backref='blogs',passive_deletes= True,lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.blog}'


class Comment(db.Model): 
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    writer = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable=False)
    blog_id= db.Column(db.Integer,db.ForeignKey('blogs.id',ondelete="CASCADE"),nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.comment}'

   



