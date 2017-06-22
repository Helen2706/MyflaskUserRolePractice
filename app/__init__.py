#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    # 附加路由和自定义错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    return app