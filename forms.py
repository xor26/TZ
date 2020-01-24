from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired


class UserAddForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    photo = FileField("Photo", validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit = SubmitField('Add')
