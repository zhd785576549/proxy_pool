from conf import settings
from mongoengine import connect


def init_db():
    """
    Initialize mongodb
    :return:
    """
    connect(
        db=settings.DATABASE["NAME"],
        # username=settings.DATABASE["USER"],
        # password=settings.DATABASE["PASSWORD"],
        host=settings.DATABASE["HOST"],
        port=int(settings.DATABASE["PORT"]),
        connect=False
    )
