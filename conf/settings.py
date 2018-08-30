import os

BASE_DIR = os.path.pardir(os.path.dirname(os.path.dirname(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logger")

DATABASE = {
    "ENGINE": "mysql",
    "USER": "spider_proxies",
    "PASSWORD": "spider_proxies",
    "HOST": "localhost",
    "PORT": "3306",
    "NAME": "spider_proxies"
}
