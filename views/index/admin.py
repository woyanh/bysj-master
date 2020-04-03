from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import current_user,login_required
from utils import admin_required,redirect_back
from models import Student,Teacher,Course,Banji,User
from extensions import db
from forms.admin import AddStu,addCourse,addTeacher,addBanji

index_admin_bp = Blueprint('index_admin',__name__)

@index_admin_bp.route('/')
@login_required
@admin_required
def index_admin():
    return render_template('admin/index.html')

@index_admin_bp.route('/manage_teacher')
@login_required
@admin_required
def manage_teacher():
    teachers = Teacher.query.all()
    return render_template('admin/manage_teacher.html',teachers=teachers)

@index_admin_bp.route('/add_teacher',methods=['GET','POST'])
@login_required
@admin_required
def add_teacher():
    form = addTeacher()
    if form.validate_on_submit():
        new_teacher = Teacher()
        new_teacher.id = form.id.data
        new_teacher.name = form.name.data
        db.session.add(new_teacher)

        new_user = User()
        new_user.id = form.id.data
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('添加老师成功','success')
        return redirect(url_for('index_admin.manage_teacher'))
    return render_template('admin/add_teacher.html',form=form)



@login_required
@admin_required
def edit_teacher():
    pass

@index_admin_bp.route('/delete_teacher/<int:id>',methods=['POST'])
@login_required
@admin_required
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    user = User.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.delete(user)
    db.session.commit()
    flash('删除成功','success')
    return redirect_back()

@index_admin_bp.route('/manage_stu')
@login_required
@admin_required
def manage_stu():
    students = Student.query.all()
    return render_template('admin/manage_stu.html',students=students)

@index_admin_bp.route('/add_stu',methods=['GET','POST'])
@login_required
@admin_required
def add_stu():
    form = AddStu()
    banji = Banji.query.all()
    form.banji.choices = [(bj.id,bj.name) for bj in banji]
    if form.validate_on_submit():
        new_stu = Student()
        new_stu.id = form.id.data
        new_stu.name = form.name.data
        new_stu.banji = Banji.query.filter_by(id=form.banji.data).first()

        new_user = User()
        new_user.id = form.id.data
        new_user.set_password(form.password.data)

        db.session.add(new_stu)
        db.session.add(new_user)
        db.session.commit()

        flash('添加成功','success')
        return redirect(url_for('index_admin.manage_stu'))
    return render_template('admin/add_stu.html',form=form)

@index_admin_bp.route('/edit_stu/<int:stu_id>',methods=['GET','POST'])
@login_required
@admin_required
def edit_stu(stu_id):
    form = AddStu()
    banji = Banji.query.all()
    form.banji.choices = [(bj.id, bj.name) for bj in banji]
    stu = Student.query.get_or_404(stu_id)
    user = User.query.get_or_404(stu_id)
    if form.validate_on_submit():
        stu.id = form.id.data
        stu.name = form.name.data
        stu.banji = Banji.query.filter_by(id=form.banji.data).first()

        user.id = form.id.data
        user.set_password(form.password.data)
        db.session.commit()
        flash('修改成功', 'success')
        return redirect(url_for('index_admin.manage_stu'))
    return render_template('admin/add_stu.html', form=form)

@index_admin_bp.route('/delete_stu/<int:id>',methods=['POST'])
@login_required
@admin_required
def delete_stu(id):
    stu = Student.query.get_or_404(id)
    user = User.query.get_or_404(id)
    db.session.delete(stu)
    db.session.delete(user)
    db.session.commit()
    flash('删除成功','success')
    return redirect_back()


@index_admin_bp.route('/manage_course')
@login_required
@admin_required
def manage_course():
    courses = Course.query.all()
    return render_template('admin/manage_course.html',courses=courses)

@index_admin_bp.route('/add_course',methods=['GET','POST'])
@login_required
@admin_required
def add_course():
    form = addCourse()
    banji = Banji.query.all()
    teacher = Teacher.query.all()
    form.teacher.choices = [(th.id, th.name) for th in teacher]
    form.banji.choices = [(bj.id, bj.name) for bj in banji]
    if form.validate_on_submit():
        new_course = Course()
        new_course.id = form.id.data
        new_course.name = form.name.data
        new_course.place = form.place.data
        new_course.start_time = form.start_time.data
        new_course.end_time = form.end_time.data
        new_course.teacher = Teacher.query.filter_by(id=form.teacher.data).first()
        new_course.banji = Banji.query.filter_by(id=form.banji.data).first()
        db.session.add(new_course)
        db.session.commit()
        flash('添加成功','success')
        return redirect(url_for('index_admin.manage_course'))
    return render_template('admin/add_course.html',form=form)

@index_admin_bp.route('/delete_course/<int:id>',methods=['POST'])
@login_required
@admin_required
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash('删除成功','success')
    return redirect_back()

@index_admin_bp.route('/manage_banji')
@login_required
@admin_required
def manage_banji():
    banjis = Banji.query.all()
    return render_template('admin/manage_banji.html',banjis=banjis)

@index_admin_bp.route('/add_banji',methods=['GET','POST'])
@login_required
@admin_required
def add_banji():
    form = addBanji()
    if form.validate_on_submit():
        new_banji = Banji()
        new_banji.id = form.id.data
        new_banji.name = form.name.data
        db.session.add(new_banji)
        db.session.commit()
        flash('添加成功','success')
        return redirect(url_for('index_admin.manage_banji'))
    return render_template('admin/add_banji.html',form=form)

@index_admin_bp.route('/delete_banji/<int:id>',methods=['POST'])
@login_required
@admin_required
def delete_banji(id):
    banji = Banji.query.get_or_404(id)
    db.session.delete(banji)
    db.session.commit()
    flash('删除成功','success')
    return redirect_back()

@index_admin_bp.route('/all')
@login_required
@admin_required
def show_all():
    stu_count = Student.query.count()
    teacher_count = Teacher.query.count()
    course_count = Course.query.count()
    banji_count = Banji.query.count()
    return render_template('admin/show_people.html',banji_count=banji_count,course_count=course_count,teacher_count=teacher_count,stu_count=stu_count)

@index_admin_bp.route('/setting')
@login_required
@admin_required
def setting():
    return render_template('admin/setting.html')