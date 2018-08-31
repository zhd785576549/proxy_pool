from db.tables import HttpProxy
from mongoengine.errors import NotUniqueError
import traceback


def insert_proxy_http(**kwargs):
    ip = kwargs.pop("ip")
    port = kwargs.pop("port")
    locate = kwargs.pop("locate", None)

    http_proxy = HttpProxy()
    http_proxy.ip = ip
    http_proxy.port = port
    http_proxy.locate = locate

    try:
        http_proxy.save()
    except NotUniqueError as e:
        pass


def fetch_all():
    http_proxy_list = HttpProxy.objects.all()
    return http_proxy_list
