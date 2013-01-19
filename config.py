# coding: utf-8


_DBUSER = "xxx" # 数据库用户名
_DBPASS = "xxx" # 数据库密码
_DBHOST = "localhost" # 数据库地址
_DBNAME = "xxx" # 数据库名称

#config
SECRET_KEY = 'flaskblog'
BLOG_TITLE = 'Welcome. | My Blog'
BLOG_URL = 'http://www.demo.com'
BLOG_NAME = 'Blog'

#admin info
ADMIN_INFO = ''
ADMIN_EMAIL = ''
ADMIN_USERNAME = ''

class rec: pass

rec.database = 'mysql://%s:%s@%s/%s' % (_DBUSER, _DBPASS, _DBHOST,_DBNAME)
rec.description = u"my blog"
rec.url = 'http://www.demo.com'
rec.paged = 8
rec.archive_paged = 20
rec.admin_username = 'koon_kai'
rec.admin_email = ''
rec.admin_password = ''
rec.default_timezone = "Asia/Shanghai"
