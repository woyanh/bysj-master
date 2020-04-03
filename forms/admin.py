from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, HiddenField, ValidationError\
    ,SelectField,DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp

class AddStu(FlaskForm):
    id = StringField('请输入学生的id', validators=[DataRequired(), Length(1, 254)])
    name = StringField('请输入学生姓名',validators=[DataRequired(),Length(2,10)])
    banji = SelectField('选择学生班级',coerce=int)
    password = PasswordField('请设置学生的密码', validators=[DataRequired()])
    submit = SubmitField('提交')

class addTeacher(FlaskForm):
    id = StringField('请输入老师的id',validators=[DataRequired(),Length(1,254)])
    name = StringField('请输入老师的姓名', validators=[DataRequired(), Length(2, 10)])
    password = PasswordField('请设置老师的密码', validators=[DataRequired()])
    submit = SubmitField('提交')

class addCourse(FlaskForm):
    id = StringField('请输入课程代码', validators=[DataRequired(), Length(1, 254)])
    name = StringField('请输入课程名称', validators=[DataRequired(), Length(2, 10)])
    place = StringField('请输入上课地点',validators=[DataRequired()])
    start_time = DateTimeField('请选择上课时间',validators=[DataRequired()])
    end_time = DateTimeField('请选择下课时间', validators=[DataRequired()])
    teacher = SelectField('请选择任课老师',coerce=int)
    banji = SelectField('请选择上课班级',coerce=int)
    submit = SubmitField('提交')

class addBanji(FlaskForm):
    id = StringField('请输入班级代码', validators=[DataRequired(), Length(1, 254)])
    name = StringField('请输入班级名称', validators=[DataRequired(), Length(2, 10)])
    submit = SubmitField('提交')