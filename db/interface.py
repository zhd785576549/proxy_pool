

def insert_proxy_http(**kwargs):
    ip = kwargs.pop("ip")
    port = kwargs.pop("port")
    anonymity = kwargs.pop("anonymity", None)
    locate = kwargs.pop("locate", None)
    bo_online = kwargs.pop("bo_online", True)
