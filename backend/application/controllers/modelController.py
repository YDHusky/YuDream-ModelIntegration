import json

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.application.service.deepLearnService import getModelInfoList, editModelInfo
from backend.application.models.resultModel import Result
from backend.application.service.userService import find_user, get_user_role

model_bp = Blueprint('model', __name__)


@model_bp.route('/model/list', methods=['GET'])
@jwt_required()
def getModelList():
    return Result().success(data=getModelInfoList())


@model_bp.route('/model/edit', methods=['POST'])
@jwt_required()
def editModelInfo_route():
    username = get_jwt_identity()
    if get_user_role(username) < 3:
        return Result().fail(message='权限不足')
    data = json.loads(request.data)
    model_info = data
    model_name = data['name']
    editModelInfo(model_name, model_info)
    return Result().success()
