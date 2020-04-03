from flask import Blueprint,render_template,flash,redirect,url_for
from models import Teacher,Student,User

from flask_login import login_user,login_required,logout_user,current_user
from forms.auth import LoginForm
from utils import redirect_back


index_auth_bp = Blueprint('index_auth',__name__)

@index_auth_bp.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(id=form.id.data.lower()).first()
        if user is not None and user.validate_password(form.password.data):
            if login_user(user):
                if user.role == 1:
                    flash(Student.query.filter_by(id=form.id.data.lower()).first().name+'同学你好', 'info')
                    return redirect(url_for('index_stu.index_stu'))
                if user.role == 2:
                    flash(Teacher.query.filter_by(id=form.id.data.lower()).first().name+'老师你好','info')
                    return redirect(url_for('index_teachers.index_teachers'))
                if user.role == 3:
                    flash('管理员你好', 'info')
                    return redirect(url_for('index_admin.index_admin'))
                return redirect_back()
            else:
                flash('您的账号被锁定了.', 'warning')
                return redirect(url_for('index_main.index'))
        flash('账号或者密码错误', 'warning')
    return render_template('index/login.html',form=form)

@index_auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('注销成功','info')
    return redirect(url_for('index_main.index'))
