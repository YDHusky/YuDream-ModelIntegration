import json

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.application.models.resultModel import Result
from backend.application.service.outService import findOutResult, addOutResult, deleteOutResult, editOutResult

out_bp = Blueprint('out', __name__)


@out_bp.route('/out/user', methods=['POST'])
@jwt_required()
def getWorksByUser():
    username = get_jwt_identity()
    return Result().success(data=findOutResult(username))


@out_bp.route('/out/save', methods=['POST'])
@jwt_required()
def saveWorks():
    username = get_jwt_identity()
    data = json.loads(request.data)
    url = data.get('url')
    work_name = data.get('work_name')
    return Result().success(data=addOutResult(username, url, work_name))


@out_bp.route('/out/delete', methods=['POST'])
@jwt_required()
def deleteWorks():
    username = get_jwt_identity()
    data = json.loads(request.data)
    id = data.get('id')
    return Result().success(data=deleteOutResult(id,username))


@out_bp.route('/out/edit', methods=['POST'])
@jwt_required()
def editWorks():
    username = get_jwt_identity()
    data = json.loads(request.data)
    id = data.get('id')
    work_name = data.get('work_name')
    return Result().success(data=editOutResult(id, work_name, username))
