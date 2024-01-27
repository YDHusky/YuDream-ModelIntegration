BASE_URL = 'http://127.0.0.1:8090'
UPLOAD_PATH = './backend/application/static/conversion/in'
CONVERSION_PATH = './backend/application/static/conversion/out'
MODEL_DIR = './backend/application/deepLearn/'
AVTAR_PATH = './backend/application/static/images/user/avatar'

class BaseConfig(object):
    SELECT_KEY = 'YUDREAM'
    JWT_SECRET_KEY = 'YUDREAM'
    DEBUG = False
    TESTING = False
    STATIC_FOLDER = './application/static'
    STATIC_URL_PATH = 'static'

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:yd901455@localhost/yudream'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
