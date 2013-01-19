# coding: utf-8
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from database import init_db
from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config)


def register_blueprints(app):
    # Prevents circular imports
    from views import posts
    from views import reply
    from views import user
    #from views import admin
    app.register_blueprint(posts)
    app.register_blueprint(reply)
    app.register_blueprint(user)

register_blueprints(app)
"""
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()
"""

#from gevent.wsgi import WSGIServer

#http_server = WSGIServer(('',8888),app)
#http_server.serve_forever()


if __name__ == '__main__':
    #init_db()
    app.run(debug=True)
