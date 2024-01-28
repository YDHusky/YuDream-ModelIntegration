import json
import os

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename

from backend.application.config import AVTAR_PATH
from backend.application.models.resultModel import Result
from backend.application.service.userService import *

user_bp = Blueprint('user', __name__, static_folder='../static/image/user')

'''
    用户模块
'''


# 用户注册
@user_bp.route('/add', methods=['POST'])
def add():
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')
    nickname = data.get('nickname')
    phone = data.get('phone')
    if find_username_or_phone_is_exist(username, phone):
        return Result().fail(message='用户名或手机号已存在', data={
            'username': username,
            'phone': phone
        })
    user = add_user(username, password, nickname, phone)
    return Result().success(data=user)


# 获取用户列表
@user_bp.route('/list', methods=['GET'])
@jwt_required()
def getUser():
    username = get_jwt_identity()
    if get_user_role(username) < 3:
        return Result().fail(message='权限不足')
    return Result().success(data=find_all())


# 用户登录
@user_bp.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')
    user = login_user(username, password)
    if user:
        return Result().success(data=user)
    else:
        return Result().fail(message='用户名或密码错误', data={
            'username': username,
            'password': password
        })


# 获取用户信息
@user_bp.route('/info', methods=['GET'])
@jwt_required()
def info():
    username = get_jwt_identity()
    user = find_user(username)
    if user:
        return Result().success(data=user.to_json())
    else:
        return Result().fail(message='用户不存在', data={
            'username': username
        })


@user_bp.route('/info/update/avtar', methods=['POST'])
@jwt_required()
def info_update_avatar():
    username = get_jwt_identity()
    user = find_user(username)
    avtar_img = request.files.getlist("avtar")
    for avtar in avtar_img:
        filename = secure_filename(avtar.filename)
        suffix = filename.split('.')[-1]
        save_name = username + '_' + time.time().__str__() + '.' + suffix
        avtar.save(os.path.join(AVTAR_PATH, save_name))
        user.avatar = f"{BASE_URL}/static/images/user/avatar/{save_name}"
        db.session.commit()
        return Result().success(data=user.to_json())


@user_bp.route('/info/update', methods=['POST'])
@jwt_required()
def info_update_base():
    username = get_jwt_identity()
    data = json.loads(request.data)
    nickname = data.get('nickname')
    email = data.get('email')
    phone = data.get('phone')
    return Result().success(data=update_user_info(username, nickname, phone, email))


@user_bp.route('/info/admin/update', methods=['POST'])
@jwt_required()
def info_update_admin():
    admin = get_jwt_identity()
    if get_user_role(admin) < 3:
        return Result().fail(message='权限不足')
    data = json.loads(request.data)
    username = data.get('username')
    nickname = data.get('nickname')
    email = data.get('email')
    phone = data.get('phone')
    role = data.get('role')
    return Result().success(data=update_user_admin(username, nickname, phone, email, role))


@user_bp.route('/info/update/password', methods=['POST'])
@jwt_required()
def info_update_password():
    username = get_jwt_identity()
    data = json.loads(request.data)
    password = data.get('old_password')
    new_password = data.get('new_password')
    return Result().success(data=update_password(username, password, new_password))


@user_bp.route('/info/admin/password', methods=['POST'])
@jwt_required()
def info_admin_password():
    admin = get_jwt_identity()
    if get_user_role(admin) < 3:
        return Result().fail(message='权限不足')
    data = json.loads(request.data)
    username = data.get('username')
    new_password = data.get('password')
    return Result().success(data=update_password_by_admin(username, new_password))


@user_bp.route('/info/username', methods=['POST'])
@jwt_required()
def info_username():
    username = get_jwt_identity()
    if get_user_role(username) < 3:
        return Result().fail(message='权限不足')
    data = json.loads(request.data)

    user = find_user(data.get('username'))
    if user is None:
        return Result().fail(message='用户不存在')
    return Result().success(data=[user.to_json()])


@user_bp.route('/info/delete', methods=['POST'])
@jwt_required()
def info_delete():
    username = get_jwt_identity()
    if get_user_role(username) < 3:
        return Result().fail(message='权限不足')
    data = json.loads(request.data)
    username = data.get('username')
    return Result().success(data=delete_user(username))


@user_bp.route('/info/admin/add', methods=['POST'])
@jwt_required()
def info_admin_add():
    admin = get_jwt_identity()
    if get_user_role(admin) < 3:
        return Result().fail(message='权限不足')
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')
    nickname = data.get('nickname')
    phone = data.get('phone')
    email = data.get('email')
    role = data.get('role')
    if find_username_or_phone_is_exist(username, phone):
        return Result().fail(message='用户名或手机号已存在', data={
            'username': username,
            'phone': phone
        })
    user = add_user(username=username, password=password, nickname=nickname, phone=phone, email=email, role=role)
    return Result().success(data=user)
