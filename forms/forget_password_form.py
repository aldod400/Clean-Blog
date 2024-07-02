from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from forms.custom_validation import MatchEmail

class ResetForm(FlaskForm):
    email = EmailField('email',
                       validators=[
                            DataRequired('Please enter your email'),
                            Email('Please enter a valid email'),
                            MatchEmail(),
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
    
    confirm_password = PasswordField('confirm_password',
                            validators=[
                                DataRequired('Please repeate your password'),
                                EqualTo('password', message='Passwords must match'),
                                    ],
                                    render_kw= {
                                        "class"       : "form-control form-control-lg",
                                        "placeholder" : "Enter a confirm password"
                                    })
    
    reset = SubmitField('Reset',
                        render_kw={
                            "class"                : "btn btn-primary btn-lg",
                            "style"                : "padding-left: 2.5rem; padding-right: 2.5rem",
                            "data-mdb-button-init" : "",
                            "data-mdb-ripple-init" : ""
                        })