from flask import Blueprint
from flask_jwt_extended import jwt_required
from backend.application.service.deepLearnService import getModelInfoList
from backend.application.models.resultModel import Result

model_bp = Blueprint('model', __name__)


@model_bp.route('/model/list', methods=['GET'])
@jwt_required()
def getModelList():
    return Result().success(data=getModelInfoList())
