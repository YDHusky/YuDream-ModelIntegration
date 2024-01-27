from backend.application.models.outModel import OutResult


def statisticsData(username):
    data = OutResult.query.filter(OutResult.username == username).all()
    return {
        "works": len(data)
    }