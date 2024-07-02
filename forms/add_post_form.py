from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileRequired, FileAllowed

class AddPost(FlaskForm):
    title = StringField('title',
                       validators=[
                            DataRequired('Please enter the title'),
                            Length(max=150),
                            ],
                           render_kw={
                                "class"       : "form-control",
                                "placeholder" : "Enter the title..."
                                })
    
    description = TextAreaField('description',
                            validators=[
                                DataRequired('Please enter the description'),
                                    ],
                                    render_kw= {
                                        "class"       : "form-control",
                                        "placeholder" : "Enter description",
                                        "style"       : "height: 12rem"
                                    })
    
    image = FileField('image',
                    validators=[
                        FileRequired('Please choose the photo'),
                        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
                        ],
                        render_kw={
                            "class" : "form-control"
                        })

    submit = SubmitField('Add',
                        render_kw={
                            "class"                : "btn btn-primary btn-lg",
                            "style"                : "padding-left: 2.5rem; padding-right: 2.5rem",
                            "data-mdb-button-init" : "",
                            "data-mdb-ripple-init" : ""
                        })