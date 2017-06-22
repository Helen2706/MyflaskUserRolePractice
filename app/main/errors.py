# coding:utf8
from . import main

# @mian.errorhandler只能定义蓝本内的错误触发程序，要想定义全局的错误处理程序，必须使用app_errorhandler


@main.app_errorhandler(404)
def page_not_found(e):
    return "页面找不到了"


@main.app_errorhandler(500)
def internal_server_error(e):
    return "服务器内部错误"