# coding: utf-8

import time
from flask  import Flask,request,session,g,redirect,url_for,Blueprint
from flask import abort,render_template,flash

import config
from helpers import getAvatar, getDay, getMonth, formatDate, formatDate2, showPost, replyContent
from database import db
import markdown

from models import Post, Reply
import base
import sqlalchemy as sa

config = config.rec()

posts = Blueprint('posts', __name__)

@posts.route('/',defaults={'page': 1})
@posts.route('/<page>')
def home(page):
    #print page
    try:
        page = int(page)
    except ValueError: 
        page = 1
    #page = int(page)
    count = db.query(Post).count();
    page_count = (count + config.paged - 1) // config.paged
    posts = db.query(Post).order_by(sa.desc(Post.created_date)).offset((page - 1) *
            config.paged).limit(config.paged)
    recent_replys = db.query(Reply).order_by(sa.desc(Reply.created_date)).limit(6)
    return render_template("home.html", posts=posts, getDay=getDay, getMonth=getMonth, \
            getAvatar=getAvatar, replyContent=replyContent, formatDate=formatDate, formatDate2=formatDate2, showPost=showPost, page=page,
            page_count=page_count, recent_replys=recent_replys)


@posts.route('/post/<pid>')
def show_post(pid):
    replyer = base.replyerGet()
    if replyer is None:
        replyer = {}
        replyer['name'] = ''
        replyer['email'] = ''
        replyer['website'] = ''
    if base.currentUserGet():
        replyer = {}
        replyer['name'] = config.admin_username
        replyer['email'] = config.admin_email
        replyer['website'] = config.url
    post = db.query(Post).get(pid)
    if not post: abort(404)
    replys = db.query(Reply).filter(Reply.pid == pid).all()
    return render_template("post.html", post=post, replys=replys, \
            formatDate=formatDate, formatDate2=formatDate2, getAvatar=getAvatar, replyer=replyer)


@posts.route('/archive')
@posts.route('/archive/page/<page>')
def list_archive(page = 1):
    #print page 
    try:
        page = int(page)
    except ValueError: 
        page = 1
    #page = int(page)
    count = db.query(Post).count()
    page_count = (count + config.archive_paged - 1) // config.archive_paged
    posts = db.query(Post).order_by(sa.desc(Post.created_date)).offset((page - 1) *
            config.archive_paged).limit(config.archive_paged)
    return render_template("archive.html", posts=posts, formatDate2=formatDate2, page=page,
             page_count=page_count, getAvatar=getAvatar)



@posts.route('/post/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'GET':
        base.checkAdmin()
        return render_template("postadd.html", getAvatar=getAvatar)

    base.checkAdmin()
    title = request.form["post[title]"]
    origin_content = request.form["post[content]"]
    content = markdown.markdown(origin_content)
    if title != '' and origin_content != '':
        db.add(Post(title=title, content=content,
            origin_content=origin_content))
        db.commit()
        return redirect("/")
    else:
        return render_template("postadd.html", error=u"标题或内容不能为空。",getAvatar=getAvatar)


@posts.route('/post/edit/<pid>',methods=['GET', 'POST'])
def edit_post(pid):
    if request.method == 'GET':
        base.checkAdmin()
        post = db.query(Post).get(pid)
        if post is None:
            abort(404)
        return render_template("postedit.html", post=post,getAvatar=getAvatar)

    base.checkAdmin()
    title = request.form["post[title]"]
    origin_content = request.form["post[content]"]
    content = markdown.markdown(origin_content)
    if title != '' and origin_content != '':
        post = db.query(Post).get(pid)
        post.title = title
        post.origin_content = origin_content
        post.content = content
        db.commit()
        return redirect("/post/%d" % (int(pid)))
    else:
        return render_template("postedit.html", error=u"标题或内容不能为空。",getAvatar=getAvatar)