from flask import Blueprint,render_template,flash,redirect,url_for,send_from_directory,current_app
from flask_login import current_user


from models import Student,Course
from forms.students import UploadAvatarForm,CropAvatarForm
from extensions import avatars,db
from utils import flash_errors


index_stu_bp = Blueprint('index_stu',__name__)

@index_stu_bp.route('/')
def index_stu():
    return render_template('stu/student.html')

@index_stu_bp.route('/mycourse')
def course():
    return render_template('stu/course.html')

@index_stu_bp.route('/myinfo')
def info():
    info = Student.query.filter_by(id=current_user.id).first()
    return render_template('stu/info.html',info=info)

@index_stu_bp.route('/setting')
def setting():
    upload_form = UploadAvatarForm()
    crop_form = CropAvatarForm()
    return render_template('stu/setting.html', upload_form=upload_form, crop_form=crop_form)

@index_stu_bp.route('/setting/upload',methods=['POST'])
def upload_avatar():
    form = UploadAvatarForm()
    if form.validate_on_submit():
        image = form.image.data
        filename = avatars.save_avatar(image)
        stu_pic = Student.query.filter_by(id = current_user.id).first()
        stu_pic.pic = filename
        #db.session.add(stu_pic)
        db.session.commit()
        flash('Image uploaded, please crop.', 'success')
    flash_errors(form)
    return redirect(url_for('.setting'))

@index_stu_bp.route('/setting/<path:filename>')
def get_avatar(filename):
    return send_from_directory(current_app.config['AVATARS_SAVE_PATH'], filename)

@index_stu_bp.route('/settings/avatar/crop', methods=['POST'])
def crop_avatar():
    form = CropAvatarForm()
    if form.validate_on_submit():
        x = form.x.data
        y = form.y.data
        w = form.w.data
        h = form.h.data
        stu_pic = Student.query.filter_by(id=current_user.id).first()
        filenames = avatars.crop_avatar(stu_pic.pic, x, y, w, h)
        stu_pic.pic_s = filenames[0]
        stu_pic.pic_m = filenames[1]
        stu_pic.pic_l = filenames[2]
        #db.session.add(stu_pic)
        db.session.commit()
        flash('Avatar updated.', 'success')
    flash_errors(form)
    return redirect(url_for('.setting'))
