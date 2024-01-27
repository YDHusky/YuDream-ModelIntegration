import time
from hashlib import md5

from backend.application.extensions import db
from backend.application.models.userModel import User
from backend.application.config import BASE_URL
from flask_jwt_extended import create_access_token


def find_user(info):
    user = User.query.filter_by(username=info).first()
    if user:
        return user
    user = User.query.filter_by(phone=info).first()
    if user:
        return user
    user = User.query.filter_by(email=info).first()
    return user


def find_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def find_all():
    users = User.query.all()
    data = [i.to_json() for i in users]
    return data


def add_user(username, password, nickname, phone=None, email=None, role=1, status=1,
             avatar=BASE_URL + '/static/images/user/default_avatar.jpg'):
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user = User(username=username, password=md5(password.encode()).hexdigest(), nickname=nickname, phone=phone,
                email=email, role=role,
                create_time=create_time, update_time=create_time,
                avatar=avatar, status=status)
    db.session.add(user)
    db.session.commit()
    return user.to_json()


def find_username_or_phone_is_exist(username, phone):
    user = User.query.filter(User.username == username or User.phone == phone).first()
    if user:
        return True
    else:
        return False


def login_user(info, password):
    user = find_user(info)
    if user and (user.password == md5(password.encode()).hexdigest()):
        token = create_access_token(identity=user.username)
        data = user.to_json()
        data['token'] = token
        return data
    else:
        return None


def get_user_role(username):
    user = find_user(username)
    if user:
        return user.role
    else:
        return None
