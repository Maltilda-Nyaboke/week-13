from . import db
from werkzeug.security import generate_password_hash,check_password_hash




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),nullable=False,unique=True)
    bio = db.Column(db.String(255))
    password = db.Column(db.String(255),nullable=False,unique=True)
    profile_pic_path = db.Column(db.String())
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    blog = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(255))
    users = db.relationship('User', backref='comments',lazy= "dynamic")


    
    
    
    
    def __repr__(self):
        return f'User {self.comment}'
       



    