import json

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.application.models.resultModel import Result
from backend.application.service.optionService import getOption, setOption
from backend.application.service.userService import find_user, get_user_role

option_bp = Blueprint('option', __name__)


@option_bp.route('/option', methods=['POST'])
@jwt_required()
def getOptionByKey():
    data = json.loads(request.data)
    key = data.get('key')
    return Result().success(data=getOption(key))


@option_bp.route('/option/update', methods=['POST'])
@jwt_required()
def updateOption():
    username = get_jwt_identity()
    data = json.loads(request.data)
    key = data.get('key')
    value = data.get('value')
    if get_user_role(username) < 3:
        return Result().fail(message='权限不足')
    return Result().success(data=setOption(key, value))
