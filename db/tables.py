from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Boolean
from db import Model
from datetime import datetime


class Proxy(Model):

    __tablename__ = "proxy_http"

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    ip = Column(String(30), nullable=False, unique=True)
    port = Column(String(10), nullable=False)
    anonymity = Column(Integer, nullable=True)
    locate = Column(String(255), nullable=True)
    speed = Column(Float, nullable=True)
    bo_online = Column(Boolean, nullable=False, default=True)
    verify_at = Column(DateTime, default=datetime.utcnow)
    create_at = Column(DateTime, default=datetime.utcnow)
    update_at = Column(DateTime, default=datetime.utcnow)
