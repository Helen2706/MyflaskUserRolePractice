 #coding:utf-8

from .. import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User',backref='role',lazy='dynamic')

    def __init__(self,name):
        self.name = name

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.WRITE|Permission.COMMENT),
            'Manager': (Permission.WRITE|Permission.COMMENT|Permission.MANAGE),
            'Administrator': (0xff)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r]
            db.session.add(role)
        db.session.commit()



class Permission:
    WRITE = 0X01
    COMMENT = 0X02
    MANAGE = 0X04
    ADMINSTER = 0X80


# 定义检查用户权限的自定义修饰器
from functools import wraps
from flask import abort
from flask_login import current_user

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args,**kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args,**kwargs)
        return decorated_function
    return decorator()

def admin_required(f):
    return permission_required(Permission.ADMINSTER)(f)
