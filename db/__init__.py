from conf import settings
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "{engine}://{user}:{password}://{host}:{port}/{name}?charset=utf8".format(
    engine=settings.DATABASE["ENGINE"],
    user=settings.DATABASE["USER"],
    password=settings.DATABASE["PASSWORD"],
    host=settings.DATABASE["HOST"],
    port=settings.DATABASE["PORT"],
    name=settings.DATABASE["NAME"],
)

engine = create_engine(db_url, pool_size=100, encoding='utf8')
Session = sessionmaker(bind=engine)
Model = declarative_base()
