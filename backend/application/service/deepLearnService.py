import os

from backend.application.config import MODEL_DIR
from backend.application.models.deepLearningModel import readModelMeta


def getModelInfoList():
    model_info = []
    for model in os.listdir(MODEL_DIR):
        if os.path.isdir(os.path.join(MODEL_DIR, model)):
            meta = readModelMeta(os.path.join(MODEL_DIR, model, 'meta.json'))
            model_info.append({
                "name": meta['name'],
                "displayName": meta['displayName'],
                "description": meta['description'],
                "author": meta['author'],
                "version": meta['version'],
                "modelDir": model
            })
    return model_info


def getModel(model_name):
    for model in getModelInfoList():
        if model['name'] == model_name:
            return model['modelDir']
