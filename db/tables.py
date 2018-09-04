from mongoengine import Document
from mongoengine import IntField
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import DateTimeField
from mongoengine import FloatField
from mongoengine import ReferenceField
from mongoengine import URLField
import datetime


class HttpProxy(Document):
    ip = StringField(max_length=20, unique=True, null=False)                # ip address
    port = StringField(max_length=10, unique=False, null=False)             # port
    locate = StringField(max_length=200)                                      # proxy address
    create_at = DateTimeField(default=datetime.datetime.now)                  # create time
    update_at = DateTimeField(default=datetime.datetime.now)                  # update time

    def __str__(self):
        return "{0}:{1}".format(self.ip, self.port)

    meta = {
        'collection': 'http_proxy'
    }


class VerifyProject(Document):

    name = StringField(max_length=100, unique=True, null=False)         # project name
    target = URLField(null=False)                           # test url with proxy
    timeout = IntField(default=0)                           # request timeout 0: no timeout, other: seconds
    headers = StringField(max_length=1000, null=False)      # request header
    proxy_type = IntField(default=0)                        # proxy http 0: http, 1: https
    bo_enable = BooleanField(default=True)                  # whether enabled
    brief = StringField(max_length=200, null=True)           # project brief
    create_at = DateTimeField(default=datetime.datetime.now)  # create time
    update_at = DateTimeField(default=datetime.datetime.now)  # update time

    def __str__(self):
        return self.name

    meta = {
        'collection': 'verify_project'
    }


class HttpProxyQuality(Document):
    verify_project = ReferenceField(VerifyProject)      # verify project
    speed = FloatField()      # test speed of reach page with proxy
    http_proxy = ReferenceField(HttpProxy)
    create_at = DateTimeField(default=datetime.datetime.now)      # create time
    update_at = DateTimeField(default=datetime.datetime.now)      # update time

    meta = {
        'collection': 'http_proxy_quality'
    }


class Logger(Document):
    # id = IntField(primary_key=True, unique=True, null=False)   # primary key
    level = StringField(max_length=10, null=False)      # log level: debug, info, warn, error
    module = StringField(max_length=20, null=False)     # log module
    filename = StringField(max_length=20, null=False)   # log filename
    message = StringField(max_length=1000, null=True)   # log message
    create_at = DateTimeField(default=datetime.datetime.now)    # create time

    meta = {
        'collection': 'logger'
    }


class User(Document):
    username = StringField(max_length=200, unique=True, null=False)     # username
    password = StringField(max_length=200, null=False)      # password md5 encode
    is_superuser = BooleanField(default=False)              # whether superuser or not
    is_staff = BooleanField(default=False)                   # whether can enter backend
    create_at = DateTimeField(default=datetime.datetime.now)  # create time
    update_at = DateTimeField(default=datetime.datetime.now)  # update time

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    meta = {
        'collection': 'user'
    }
