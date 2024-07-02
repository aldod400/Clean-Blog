from flask import Blueprint, render_template, redirect, url_for, request, session
from config import db
from models.post import Posts

home = Blueprint('home', __name__)

@home.route('/')
def index():
    posts = Posts.query.all()
    return render_template('home.html', title = 'Home', image_path = 'static/assets/img/home-bg.jpg', posts = posts)