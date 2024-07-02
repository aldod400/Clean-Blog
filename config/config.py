import os


class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/db_blogs'
    UPLOAD_FOLDER = 'static/assets/img'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    Flask_APP= 'run.py'
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = './.flask_session/'
    

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}   

