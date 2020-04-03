from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class Face(db.Model):
    token = db.Column(db.Integer,primary_key=True,unique=True)
    belong2 = db.Column(db.Integer) #这个token所属于的学生的id
    upload_pic = db.Column(db.String)

class Upload_Face(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True) #上传的照片id
    pic_name = db.Column(db.String) #上传的照片名字
    course = db.Column(db.Integer)

class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    name = db.Column(db.String(20))
    place = db.Column(db.String(20))#数据库里面还没有添加，稍后添加
    start_time = db.Column(db.DateTime,default=datetime(2008,8,8))
    end_time = db.Column(db.DateTime,default=datetime(2008,8,9))
    stu_check_time = db.Column(db.DateTime,default=datetime(2008,8,10))

    #老师和课程的一对多关系
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))
    teacher = db.relationship('Teacher',back_populates='courses')

    #班级和课程的一对多关系
    banji_id = db.Column(db.Integer,db.ForeignKey('banji.id'))
    banji = db.relationship('Banji',back_populates='courses')

class Banji(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    name = db.Column(db.String(20))

    #这里是学生和班级的一对多关系
    students = db.relationship('Student',back_populates='banji')

    #班级和课程的一对多关系
    courses = db.relationship('Course',back_populates='banji')

class Teacher(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    name = db.Column(db.String(20))

    #老师和课程的一对多关系
    courses = db.relationship('Course',back_populates='teacher')

class Student(db.Model):
    id = db.Column(db.Integer,unique=True,primary_key=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(10))

    #没有添加到数据库
    pic = db.Column(db.String(512))
    pic_s = db.Column(db.String(64))
    pic_m = db.Column(db.String(64))
    pic_l = db.Column(db.String(64))

    check_time = db.Column(db.DateTime,default=datetime(2008,8,7))

    # 这里是学生和班级的一对多关
    class_id = db.Column(db.Integer,db.ForeignKey('banji.id'))
    banji = db.relationship('Banji',back_populates='students')

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    password_hash = db.Column(db.String(128))
    #pic = db.Column(db.String(64))

    role = db.Column(db.Integer,default=1)#1是学生，2是老师，3是管理员

    # 设置密码
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # 验证密码
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)





