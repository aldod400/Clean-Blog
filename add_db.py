from config.db import db
from run import app
from models.user import Users
from models.post import Posts
import os

with app.app_context():
    # db.create_all()
    # student1 = Users(name = "aldod", email = "aldod@gmail.com", password = "12121212")
    # db.session.add(student1)
    # db.session.commit()

    # user = Users.query.filter_by(email = "aldod").first()
    # user.password = "12312"
    # db.session.commit()
    # print(user.email)
    pass