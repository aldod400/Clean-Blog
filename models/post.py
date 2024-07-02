from config import db
from datetime import datetime

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    slug = db.Column(db.String(100), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = True)
    image_path = db.Column(db.Text, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    