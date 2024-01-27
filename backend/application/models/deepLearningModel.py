import json
import os.path

import cv2
import numpy as np
import tensorflow as tf

from backend.application.config import MODEL_DIR


def readModelMeta(meta_path):
    with open(meta_path, 'r', encoding='utf-8') as f:
        meta = json.loads(f.read())
    return meta


def saveImg(img, img_out_path):
    result = np.squeeze(img)
    output_mask = result * 255.
    output_mask = np.clip(output_mask, 0, 255)
    output_image = cv2.cvtColor(output_mask.astype('uint8'), cv2.COLOR_BGR2RGB)
    cv2.imwrite(str(img_out_path), output_image)


class DeepLearningModel:
    def __init__(self, model_dir):
        self.meta = readModelMeta(os.path.join(MODEL_DIR, model_dir, 'meta.json'))
        # self.meta = readModelMeta(os.path.join('../deepLearn', model_dir, 'meta.json'))
        self.name = self.meta['name']
        self.display_name = self.meta['displayName']
        self.description = self.meta['description']
        self.author = self.meta['author']
        self.version = self.meta['version']
        self.in_shape = self.meta['inShape']
        self.out_shape = self.meta['outShape']
        self.model_dir = os.path.join(MODEL_DIR, model_dir, 'savedmodel')
        # self.model_dir = os.path.join('../deepLearn', model_dir, 'savedmodel')
        self.interpreter = tf.saved_model.load(self.model_dir)
        self.infer = self.interpreter.signatures["serving_default"]

    def in_image(self, img_path):
        h, w = self.in_shape[1], self.in_shape[2]
        img = cv2.imread(img_path).astype(np.float32)
        i_h = img.shape[0]
        i_w = img.shape[1]
        if h is None and w is None:
            return img
        if h is None and w is not None:
            new_w = w
            new_h = int(new_w / i_w * i_h)
            return cv2.resize(img, (new_w, new_h))
        if h is not None and w is None:
            new_h = h
            new_w = int(new_h / i_h * i_w)
            return cv2.resize(img, (new_w, new_h))
        if h is not None and w is not None:
            return cv2.resize(img, (w, h))

    def loadImage(self, img_path):
        img = self.in_image(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.expand_dims(img, axis=0)
        return img

    def handle(self, img_path, out_path):
        sample_image = np.asarray(self.loadImage(img_path))
        output_data = self.infer(tf.constant(sample_image))
        result = output_data['output_tensor'].numpy()
        saveImg(result, out_path)
