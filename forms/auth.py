from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,RadioField,SelectField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

class LoginForm(FlaskForm):
    id = StringField('请输入您的账号', validators=[DataRequired(), Length(1, 254)])
    password = PasswordField('请输入密码', validators=[DataRequired()])
    submit = SubmitField('登陆')