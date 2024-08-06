from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from config import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    stats = db.relationship('Books', backref='users', lazy=True )

    def to_json(self):
        return{
            "id":self.id,
            "email":self.email,
            "password":self.password
        }
    
class Books(db.Model):
    __tablename__ = 'books'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "user_id": self.user_id  # Include user_id if needed
        }