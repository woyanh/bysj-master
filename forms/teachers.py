from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, HiddenField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp


class imgUpload(FlaskForm):
    image = FileField('上传', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'The file format should be .jpg or .png.')])
    submit = SubmitField('自动识别')
