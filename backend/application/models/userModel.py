from backend.application.extensions import db


def find_by_username(username):
    return User.query.filter_by(username=username).first()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 昵称
    nickname = db.Column(db.String(255))
    # 用户名
    username = db.Column(db.String(255))
    # 密码
    password = db.Column(db.String(255))
    # 邮箱
    email = db.Column(db.String(255))
    # 手机号
    phone = db.Column(db.String(255))
    # 状态
    status = db.Column(db.Integer, default=1)
    # 角色
    role = db.Column(db.Integer, default=1)
    # 创建时间
    create_time = db.Column(db.DateTime)
    # 更新时间
    update_time = db.Column(db.DateTime)
    # 是否删除
    is_delete = db.Column(db.Integer, default=0)
    # 头像
    avatar = db.Column(db.String(255))

    def to_json(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'status': self.status,
            'role': self.role,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'is_delete': self.is_delete,
            'avatar': self.avatar
        }

