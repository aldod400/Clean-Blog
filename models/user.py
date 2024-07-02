from config import db
from models.post import Posts
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable=False)
    post = db.relationship('Posts', backref = "user")