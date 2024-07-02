from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email
from forms.custom_validation import MatchEmailAndPassword

class LoginForm(FlaskForm):
    email = EmailField('email',
                       validators=[
                            DataRequired('Please enter your email'),
                            Email('Please enter a valid email'),
                            MatchEmailAndPassword(),
                            ],
                           render_kw={
                                "class"       : "form-control form-control-lg",
                                "placeholder" : "Enter a valid email address"
                                })
    
    password = PasswordField('password',
                            validators=[
                                DataRequired('Please enter your password'),
                                Length(min=8,max=25, message= 'password must be at least 8 digits'),
                                    ],
                                    render_kw= {
                                        "class"       : "form-control form-control-lg",
                                        "placeholder" : "Enter password"
                                    })
    
    submit = SubmitField('Login',
                        render_kw={
                            "class"                : "btn btn-primary btn-lg",
                            "style"                : "padding-left: 2.5rem; padding-right: 2.5rem",
                            "data-mdb-button-init" : "",
                            "data-mdb-ripple-init" : ""
                        })