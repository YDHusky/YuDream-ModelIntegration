import os
import time

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from backend.application.service.deepLearnService import getModel
from backend.application.config import BASE_URL, UPLOAD_PATH, CONVERSION_PATH
from backend.application.models.deepLearningModel import DeepLearningModel

from backend.application.models.resultModel import Result

conversion_bp = Blueprint('conversion', __name__, static_folder='../static/image/conversion')

'''
    转换模块
'''


@conversion_bp.route('/image', methods=['POST'])
@jwt_required()
def upload_pic():
    username = get_jwt_identity()
    # 来获取多个上传文件
    imgs = request.files.getlist("images")
    model_name = request.form.get('model_name')
    model = DeepLearningModel(getModel(model_name))
    print(imgs)
    urls = []
    # 循环读取上传的文件并保存
    for img in imgs:
        filename = secure_filename(img.filename)
        suffix = filename.split('.')[-1]
        save_name = username + '_' + time.time().__str__() + '.' + suffix
        img.save(os.path.join(UPLOAD_PATH, save_name))
        model.handle(os.path.join(UPLOAD_PATH, save_name), os.path.join(CONVERSION_PATH, save_name))
        msg = f"{BASE_URL}/static/conversion/out/{save_name}"
        urls.append(msg)
    return Result().success(data=urls)
