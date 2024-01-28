from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.application.models.resultModel import Result
from backend.application.service.deepLearnService import getModelInfoList
from backend.application.service.outService import *
from backend.application.service.userService import find_all, get_user_role

statistics_bp = Blueprint('statistics', __name__)


@statistics_bp.route('/statistics', methods=['GET'])
@jwt_required()
def getStatistics():
    username = get_jwt_identity()
    model = len(getModelInfoList())
    work = len(findOutResult(username))
    return Result().success(data={'model': model, 'work': work})


@statistics_bp.route('/statistics/admin', methods=['GET'])
@jwt_required()
def getStatisticsAdmin():
    username = get_jwt_identity()
    if get_user_role(username) < 3:
        return Result().fail(message='权限不足')
    model = len(getModelInfoList())
    work = len(findOutAllResult())
    user = len(find_all())
    return Result().success(data={'model': model, 'work': work, 'user': user})
