# coding:utf-8
# 一个点表示当前目录，每多一个点号则代表向上一层目录。
from .. import db,login_manager
from .Role import Permission
from flask_login import UserMixin,AnonymousUserMixin


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(64))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __init__(self,username,password_hash):
        self.username = username
        self.password_hash = password_hash

    def can(self,permissions):
        return self.role is not None and \
               (self.role.permissions&permissions)==permissions

    def is_administrator(self):
        return self.can(Permission.ADMINSTER)


# 定义未定义用户类，为了更方便的对current_user调用can和is_administrator
class AnonymousUser(AnonymousUserMixin):
    def can(self,permissions):
        return False

    def is_administrator(self):
        return False

# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))