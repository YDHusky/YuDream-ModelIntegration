from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.application.models.resultModel import Result
from backend.application.service.deepLearnService import getModelInfoList
from backend.application.service.outService import findOutResult

statistics_bp = Blueprint('statistics', __name__)


@statistics_bp.route('/statistics', methods=['GET'])
@jwt_required()
def getStatistics():
    username = get_jwt_identity()
    model = len(getModelInfoList())
    work = len(findOutResult(username))
    return Result().success(data={'model': model, 'work': work})
