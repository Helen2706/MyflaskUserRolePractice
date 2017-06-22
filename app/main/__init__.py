#coding:utf-8
from flask import Blueprint

#参数为蓝本的名字和蓝本所在的模块或包的名字
main = Blueprint('main',__name__)

from . import views