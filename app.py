import os


from flask import Flask

from extensions import db,moment,csrf,bootstrap,login_manager,register_template_global,avatars
from views.index.main import index_main_bp
from views.index.admin import index_admin_bp
from views.index.teachers import index_teachers_bp
from views.index.students import index_stu_bp
from views.index.auth import index_auth_bp

from config import config

def create_app():
    app = Flask(__name__)

    app.config.from_object(config['development'])

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_template_global(app)

    return app

def register_extensions(app):
    db.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    avatars.init_app(app)


def register_blueprints(app):
    #蓝图注册
    app.register_blueprint(index_main_bp)
    app.register_blueprint(index_admin_bp,url_prefix='/admin')
    app.register_blueprint(index_teachers_bp,url_prefix='/teacher')
    app.register_blueprint(index_stu_bp,url_prefix='/student')
    app.register_blueprint(index_auth_bp)

def register_errorhandlers(app):
    pass



