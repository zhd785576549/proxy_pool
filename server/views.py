from flask import request
from db.interface import fetch_all
import random


def fetch():
    proxy_list = fetch_all()
    ran_idx = random.randint(0, len(proxy_list))
    proxy = proxy_list[ran_idx]
    return "{0}:{1}".format(proxy.ip, proxy.port)
