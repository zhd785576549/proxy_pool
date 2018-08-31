from mongoengine import Document
from mongoengine import IntField
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import ListField
from mongoengine import DateTimeField
from mongoengine import FloatField
from mongoengine import ReferenceField
from mongoengine import URLField
import datetime


class HttpProxy(Document):
    id = IntField(primary_key=True, unique=True, null=False)                # primary key
    ip = StringField(max_length=20, unique=True, null=False)                # ip address
    port = StringField(max_length=10, unique=False, null=False)             # port
    bo_online = BooleanField(default=True)                                   # whether host can reach the proxy
    locate = StringField(max_length=200)                                      # proxy address
    create_at = DateTimeField(default=datetime.datetime.now)                  # create time
    update_at = DateTimeField(default=datetime.datetime.now)                  # update time
    meta = {
        'collection': 'http_proxy'
    }


class HttpProxyQuality(Document):
    id = IntField(primary_key=True, unique=True, null=False)   # primary key
    anonymity = IntField()    # degree of anonymity: 1: high, 2: normal, 3: transport
    speed = FloatField()      # test speed of reach page with proxy
    bo_pass = BooleanField(default=True)   # whether host can reach the page with proxy
    http_proxy = ListField(ReferenceField(HttpProxy))  # http proxy
    quality = IntField(default=0)   # proxy quality: bo_pass==0?0,anonymity*1000+int(speed*100)
    target = URLField(null=False)   # test url with proxy
    create_at = DateTimeField(default=datetime.datetime.now)      # create time
    update_at = DateTimeField(default=datetime.datetime.now)      # update time

    meta = {
        'collection': 'http_proxy_quality'
    }
