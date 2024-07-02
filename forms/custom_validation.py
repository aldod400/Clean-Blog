from wtforms import ValidationError
from models.user import Users
from werkzeug.security import check_password_hash


class MatchEmailAndPassword(object):
     def __call__(self, form, field):
        user = Users.query.filter_by(email=field.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            raise ValidationError('the email and password dosen\'t match')
        

class UniqueEmail(object):
    def __init__(self, message=None):
        if not message:
            message = 'Email address already exists. Please use a different email.'
        self.message = message

    def __call__(self, form, field):
        user = Users.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError(self.message)


class MatchEmail(object):
     def __call__(self, form, field):
        user = Users.query.filter_by(email=field.data).first()
        if not user:
            raise ValidationError('Email not found')