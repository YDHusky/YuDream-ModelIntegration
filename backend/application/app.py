from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from backend.application.extensions import db
from backend.application.config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    JWTManager(app)
    CORS(app, origins='http://localhost:5173', supports_credentials=True)
    from backend.application.controllers.userController import user_bp
    app.register_blueprint(user_bp)
    from backend.application.controllers.conversionController import conversion_bp
    app.register_blueprint(conversion_bp)
    from backend.application.controllers.modelController import model_bp
    app.register_blueprint(model_bp)
    from backend.application.controllers.outController import out_bp
    app.register_blueprint(out_bp)
    from backend.application.controllers.statisicsController import statistics_bp
    app.register_blueprint(statistics_bp)
    from backend.application.controllers.optionController import option_bp
    app.register_blueprint(option_bp)
    return app
