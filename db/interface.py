from db.tables import Proxy
from db import Session


def insert_proxy_http(**kwargs):
    session = Session()
    ip = kwargs.pop("ip")
    port = kwargs.pop("port")
    anonymity = kwargs.pop("anonymity", None)
    locate = kwargs.pop("locate", None)
    bo_online = kwargs.pop("bo_online", True)

    proxy = Proxy()
    proxy.ip = ip
    proxy.port = port
    proxy.anonymity = anonymity
    proxy.locate = locate
    proxy.bo_online = bo_online

    try:
        session.add(proxy)
        session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.close()
