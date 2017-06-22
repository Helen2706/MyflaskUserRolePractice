# coding:utf-8
import os

#定义当前文件的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # 设置每次请求结束后自动提交数据库的变化
    SQLALCHEMY_COMMIT_ON_TEARDOWM = True
    SECRET_KEY = 'SDFEFEF'

    @staticmethod
    def init_app(app):
        pass

# 开发模式的配置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/myflasky_database"

# 测试模式的配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:1234@localhost/myfalsky_database"

# 产品发布模式的配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:1234@localhost/myfalsky_database"

#定义字典
config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig
}