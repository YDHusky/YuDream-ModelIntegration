from backend.application.extensions import db


class OutResult(db.Model):
    __tablename__ = 'out_result'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    username = db.Column(db.String(255))
    # 图片地址
    url = db.Column(db.String(255))
    # 创建时间
    create_time = db.Column(db.DateTime)
    # 是否删除
    is_delete = db.Column(db.Integer, default=0)
    # 作品名字
    work_name = db.Column(db.String(255))

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'work_name': self.work_name,
            'url': self.url,
            'create_time': self.create_time,
            'is_delete': self.is_delete
        }
