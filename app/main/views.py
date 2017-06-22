from flask import render_template
from . import main
from app.models.User import User
from app.models.Role import Role
from .. import db


@main.route('/')
def index():
    Role.insert_roles()
    role = Role.query.filter_by(name='User').first()
    user = User.query.filter_by(role=role).all()
    for user1 in user:
        print user1.username
    return render_template('main/index.html')