from flask_login import UserMixin
from . import db
from . import login_manager

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

    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):


