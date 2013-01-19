# coding: utf-8

import time
import sqlalchemy as sa
from database import Base

class Post(Base):
    __tablename__ = 'post'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }

    id = sa.Column(sa.Integer, primary_key = True, autoincrement = True)
    title = sa.Column(sa.String(64))
    content = sa.Column(sa.Text)
    origin_content = sa.Column(sa.Text)
    created_date = sa.Column(sa.Integer)
    update_date = sa.Column(sa.Integer)

    def __init__(self, title=title, content=content, origin_content=None,
            created_date=None, update_date=None):
        self.title = title
        self.content = content
        self.update_date = update_date
        if created_date == None:
            self.created_date = time.time()
        else:
            self.created_date = created_date
        if origin_content == None:
            self.origin_content = content
        else:
            self.origin_content = origin_content


    def __repr__(self):
        return '<Post %s>' % (self.title)
