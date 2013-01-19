#-*- coding:UTF-8-*-

import config

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker

config = config.rec()
engine = sa.create_engine(config.database + '?charset=utf8')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

db = db_session 

def init_db():
    import models
    Base.metadata.create_all(engine)
    print(u'数据库部署完成！')
    return
