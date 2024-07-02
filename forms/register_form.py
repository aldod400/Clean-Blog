from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from forms.custom_validation import UniqueEmail

class RegisterForm(FlaskForm):
    name = StringField('name', 
                       validators = [
                           DataRequired('Please enter your name'),
                           Length(max=40, message= "the limit of name is 40 character"),
                       ],
                       render_kw={
                           "class"       : "form-control form-control-lg",
                           'placeholder' : "Enter your name",
                       })


    email = EmailField('email',
                       validators=[
                            Email('Please enter a valid email'),
                            DataRequired('Please enter your email'),
                            UniqueEmail()
                            ],
                           render_kw={
                                "class"       : "form-control form-control-lg",
                                "placeholder" : "Enter a valid email address"
                                })
    
    password = PasswordField('password',
                            validators=[
                                Length(min=8,max=25, message= 'password must be at least 8 digits'),
                                DataRequired('Please enter your password'),
                                    ],
                                    render_kw= {
                                        "class"       : "form-control form-control-lg",
                                        "placeholder" : "Enter password"
                                    })
    
    confirm_password = PasswordField('confirm_password',
                            validators=[
                                DataRequired('Please repeate your password'),
                                EqualTo('password', message='Passwords must match'),
                                    ],
                                    render_kw= {
                                        "class"       : "form-control form-control-lg",
                                        "placeholder" : "Enter a confirm password"
                                    })

    submit = SubmitField('Register',
                        render_kw={
                            "class"                : "btn btn-primary btn-lg",
                            "style"                : "padding-left: 2.5rem; padding-right: 2.5rem",
                            "data-mdb-button-init" : "",
                            "data-mdb-ripple-init" : ""
                        })