from flask import Flask
from flask_session import Session
from config.config import config_by_name
from config.db import db
from view.auth import auth
from view.home import home
from view.blog import blog

def create_app(config_name):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    Session(app)
    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(blog)
    return app


