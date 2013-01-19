# coding: utf-8

from flask import Flask, session, redirect, url_for, request,abort
import config

config = config.rec()

def on_finish():
    None

def currentUserGet():
    if 'user' in session:
        user = session['user']
        return user['username']
    else:
        return None

def currentUserSet(username):
    if username:
        session['user'] = dict({'username':username})
    else:
        session.pop('user',None)

def replyerSet(name, email, website):
    if name:
        session['replyer'] = dict({'name': name, 'email': email,'website': website})
    else:
        session.pop('replyer',None)
      

def replyerGet():
    if 'replyer' in session:
        reply = session['replyer']
        name = reply['name']
        return name
    else:
        return None

def userAuth(username, password):
    return username == config.admin_username and password == config.admin_password

def isAdmin():
    return currentUserGet() == config.admin_username

def checkAdmin():
    if not isAdmin():
        abort(404)

def get_current_user():
    return currentUserGet()
