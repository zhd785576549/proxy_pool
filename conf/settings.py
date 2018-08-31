import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logger")

DATABASE = {
    "ENGINE": "mongodb",
    "USER": "spider_proxies",
    "PASSWORD": "spider_proxies",
    "HOST": "127.0.0.1",
    "PORT": "27017",
    "NAME": "spider_proxies"
}
