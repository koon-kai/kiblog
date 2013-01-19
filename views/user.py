# coding: utf-8

from flask  import Flask,request,session,g,redirect,url_for,Blueprint
from flask import abort,render_template,flash
from helpers import getAvatar
import config
#from .base import BaseHandler
import base
config = config.rec()

user = Blueprint('user', __name__)


#class LoginHandler(BaseHandler):
@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if base.isAdmin():
            return redirect("/")
        else:
            return render_template("login.html",getAvatar=getAvatar)
    
    username = request.form['username']
    password = request.form['password']
    if base.userAuth(username, password):
        base.currentUserSet(username)
        return redirect("/")
    else:
        return redirect("/login")

#class LogoutHandler(BaseHandler):
@user.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/login')

