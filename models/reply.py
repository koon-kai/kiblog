# coding: utf-8

import time
import sqlalchemy as sa
from database import Base


class Reply(Base):
    __tablename__ = 'reply'
    __table_args__ = {
            'mysql_charset': 'utf8',
    }

    id = sa.Column(sa.Integer, primary_key = True, autoincrement = True)
    pid = sa.Column(sa.Integer, index=True)
    name = sa.Column(sa.String(64), nullable = False)
    email = sa.Column(sa.String(100), nullable = False)
    website = sa.Column(sa.String(100))
    content = sa.Column(sa.Text)
    origin_content = sa.Column(sa.Text)
    created_date = sa.Column(sa.Integer)
    update_date = sa.Column(sa.Integer)
    number = sa.Column(sa.Integer)

    def __init__(self, pid=pid, name=name, email=email, website=website,
            content=content, origin_content=None, created_date=None,
            update_date=None, number=1):
        self.pid = pid
        self.name = name
        self.email = email
        self.website = website
        self.content = content
        self.update_date = update_date
        self.number = number
        if created_date == None:
            self.created_date = time.time()
        else:
            self.created_date = created_date
        if origin_content == None:
            self.origin_content = content
        else:
            self.origin_content = origin_content

    def __repr__(self):
        return '<Reply %d %s>' % (self.id, self.name)
