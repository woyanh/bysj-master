from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_moment import Moment
from flask_login import LoginManager
from flask_avatars import Avatars

db = SQLAlchemy()
bootstrap = Bootstrap()
csrf = CSRFProtect()
moment = Moment()
login_manager = LoginManager()
avatars = Avatars()

@login_manager.user_loader
def load_user(user_id):
    from models import User
    user = User.query.get(int(user_id))
    return user

def register_template_global(app):
    @app.template_global()
    def getname(id):
        from models import Student
        return Student.query.filter_by(id=id).first().name

    @app.template_global()
    def get_course(id):
        from models import Student
        return Student.query.filter_by(id=id).first().banji.courses

    @app.template_global()
    def get_teacher_name(id):
        from models import Teacher
        return Teacher.query.filter_by(id=id).first().name

    @app.template_global()
    def get_teacher_course(id):
        from models import Teacher
        return Teacher.query.filter_by(id=id).first().courses

    @app.template_global()
    def get_stu(id):
        from models import Student
        return Student.query.filter_by(id=id).first()