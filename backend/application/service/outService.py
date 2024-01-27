from datetime import datetime

from backend.application.extensions import db
from backend.application.models.outModel import OutResult


def addOutResult(username, url):
    out = OutResult(username=username, url=url, create_time=datetime.now())
    db.session.add(out)
    db.session.commit()
    return out.to_json()
