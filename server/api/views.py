from db.interface import fetch_all_http_proxy
import random


def fetch():
    proxy_list = fetch_all_http_proxy()
    ran_idx = random.randint(0, len(proxy_list))
    proxy = proxy_list[ran_idx]
    return "{0}:{1}".format(proxy.ip, proxy.port)
