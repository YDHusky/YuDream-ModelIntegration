import json

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

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