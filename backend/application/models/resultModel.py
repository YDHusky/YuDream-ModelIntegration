from flask import jsonify


class Result:
    def __init__(self):
        self.code = 0
        self.message = ''
        self.data = None

    def to_json(self):
        return jsonify({'code': self.code, 'message': self.message, 'data': self.data})

    def success(self, message='success', data=None):
        self.code = 200
        self.message = message
        self.data = data
        return self.to_json()

    def fail(self, message='fail', data=None):
        self.code = 500
        self.message = message
        self.data = data
        return self.to_json()

    def error(self, message='error', data=None):
        self.code = 500
        self.message = message
        self.data = data
        return self.to_json()

    def not_found(self, message='not found', data=None):
        self.code = 404
        self.message = message
        self.data = data
        return self.to_json()
