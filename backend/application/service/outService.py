from datetime import datetime

from backend.application.extensions import db
from backend.application.models.outModel import OutResult


def addOutResult(username, url, work_name):
    out = OutResult(username=username, url=url, work_name=work_name, create_time=datetime.now())
    db.session.add(out)
    db.session.commit()
    return out.to_json()


def findOutResult(username):
    data = OutResult.query.filter(OutResult.username == username).all()
    return [i.to_json() for i in data]


def deleteOutResult(work_id, username):
    data = OutResult.query.filter(OutResult.id == work_id).first()
    if data.username != username:
        return False
    db.session.delete(data)
    db.session.commit()
    return True


def editOutResult(work_id, work_name, username):
    data = OutResult.query.filter(OutResult.id == work_id).first()
    if data.username != username:
        return False
    data.work_name = work_name
    db.session.commit()
    return True


def findOutAllResult():
    data = OutResult.query.all()
    return [i.to_json() for i in data]
