# coding:utf-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


from . import user
from flask import request,redirect,render_template,url_for,flash
from app.models.User import User
from flask_login import login_user,login_required,logout_user,current_user


@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template('user/login.html')
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        user = User.query.filter_by(username=name).first()
        if user is not None and user.password_hash == password:
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash("用户名或密码错误！")
            return render_template('user/login.html')

# 注销用户
@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('已注销用户')
    return redirect(request.args.get('next') or url_for('main.index'))


