import os
import uuid
import requests
import json

from face import post_img,get_access_token,get_zb,encode
from flask import Blueprint,render_template,url_for,request,send_from_directory,current_app,redirect
from forms.teachers import imgUpload
from utils import allowed_file,random_filename
from PIL import Image,ImageDraw
from face.opreate import draw_face,save_face
from models import Face,Student,Upload_Face,Course,Banji


index_teachers_bp = Blueprint('index_teachers',__name__)

@index_teachers_bp.route('/')
def index_teachers():
    return render_template('teacher/index.html')

@index_teachers_bp.route('/details')
def count_details():
    pass

@index_teachers_bp.route('/info')
def info():
    pass

@index_teachers_bp.route('/setting')
def setting():
    return render_template('teacher/setting.html')


@index_teachers_bp.route('/rollcall/<int:course_id>',methods=['GET','POST'])
def rollcall(course_id):
    form = imgUpload()
    if form.validate_on_submit():
        img = form.image.data
        filename = random_filename('.jpg')
        img.save(os.path.join(current_app.config['BYSJ_UPLOAD_PATH'], filename))

        ###这里应该是人脸对比的地方
        stu_pic = list()
        # upload_face = Upload_Face()
        # upload_face.pic_name = filename


        # 这是我自己写的api
        #zb里面是left, bottom, top ,right
        img_encode = encode(os.path.join(current_app.config['BYSJ_UPLOAD_PATH'], filename))
        data = {'image':img_encode}
        url = 'http://ali.zerb.top:5000/face/'
        headers = {'content-type': 'application/json'}
        zb = requests.post(url,data=json.dumps(data),headers=headers).json()
        if len(zb) ==0 :
            return render_template('teacher/rollcall.html', form=form, course_id='没有人脸', filename=filename)
        img_draw = draw_face(os.path.join(current_app.config['BYSJ_UPLOAD_PATH'], filename),zb)
        faces = save_face(os.path.join(current_app.config['BYSJ_UPLOAD_PATH'], filename),zb)
        img_draw.save(os.path.join(current_app.config['BYSJ_UPLOAD_PATH'], filename))
        #需要返回一个学生自己的照片list
        return render_template('teacher/rollcall.html', form=form, course_id=course_id, filename=filename,faces=faces)

        #
        # 这是百度与api
        # zb_json = post_img(get_access_token(),encode(os.path.join(current_app.config['BYSJ_UPLOAD_PATH'], filename)))
        # img_draw = face.draw_face(img,get_zb(zb_json))
        # img_draw.save(os.path.join(current_app.config['BYSJ_UPLOAD_PATH'], filename))
        # return render_template('teacher/rollcall.html', form=form, course_id=course_id,filename=filename)

    return render_template('teacher/rollcall.html',form=form,course_id=course_id)

@index_teachers_bp.route('/get_img/<path:filename>')
def get_img(filename):
    return send_from_directory(current_app.config['BYSJ_UPLOAD_PATH'],filename)
