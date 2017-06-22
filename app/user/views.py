# coding:utf-8
from . import user
from flask import request,redirect,render_template,url_for,flash
from app.models.User import User

@user.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form.get("name")
        password = request.form.get("password")
        user = User.query.filter_by(username=name).first()
        print user.password_hash
        if user.password_hash==password:
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash = "用户名或密码错误"
            return render_template(url_for('user.login'))
    else:
        return render_template('user/login.html')
