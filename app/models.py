from . import db




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),nullable=False,unique=True)
    bio = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255),nullable=False,unique=True)
    profile_pic_path = db.Column(db.String())
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))


    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(255))
    users = db.relationship('User', backref='comments',lazy= "dynamic")

    def __repr__(self):
        return f'User {self.comment}'



    