from backend.application.extensions import db


class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(255))

    def to_json(self):
        return {
            'id': self.id,
            'key': self.key,
            'value': self.value
        }
