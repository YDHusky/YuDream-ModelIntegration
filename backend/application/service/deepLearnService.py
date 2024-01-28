import json
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


def editModelInfo(model_name, model_info):
    model_dir = getModel(model_name)
    meta = readModelMeta(os.path.join(MODEL_DIR, model_dir, 'meta.json'))
    meta['displayName'] = model_info['displayName']
    meta['description'] = model_info['description']
    meta['author'] = model_info['author']
    meta['version'] = model_info['version']
    with open(os.path.join(MODEL_DIR, model_dir, 'meta.json'), 'w') as f:
        f.write(json.dumps(meta))
    return True
