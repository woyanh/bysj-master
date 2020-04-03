import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname('__file__')))


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    # db
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'flask'
    PASSWORD = 'yh520512930'
    HOST = '101.37.76.202'
    PORT = '3306'
    DATABASE = 'test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

    BYSJ_UPLOAD_PATH = os.path.join(basedir, 'uploads')

    AVATARS_SAVE_PATH = os.path.join(BYSJ_UPLOAD_PATH, 'stu_pic')
    AVATARS_SIZE_TUPLE = (30, 100, 200)

    ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(BaseConfig.DIALECT, BaseConfig.DRIVER,
                                                              BaseConfig.USERNAME, BaseConfig.PASSWORD, BaseConfig.HOST,
                                                              BaseConfig.PORT, BaseConfig.DATABASE)


config = {
    'development': DevelopmentConfig
}
