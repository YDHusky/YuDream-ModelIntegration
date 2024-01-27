from backend.application.extensions import db
from backend.application.models.optionModel import Option


def getOption(info):
    option = Option.query.filter_by(key=info).first()
    print(option)
    if option is None:
        return None
    return option.to_json()


def setOption(key, value):
    option = Option.query.filter_by(key=key).first()
    option.value = value
    option.save()
    db.commit()
    return option.to_json()
