from logging import log
import re
from flask import Blueprint, session, render_template, request, redirect
from models import *

login = Blueprint('login', __name__)


@login.route('/', methods = ['GET'])
def SendHtmlLogin():
    if 'username' in session:
       return redirect('/') 
    return render_template('login.html')

@login.route('/', methods = ['POST'])
def CheckLogin():
    _username = request.form['username']
    _password = request.form['password']

    us = Users.select().where(Users.username == _username)
    if us.exists():
        us = Users.get(Users.username == _username)
        print(us.password, _password)
        if us.password == _password:
            session['username'] = _username
            return redirect('/')
        else:
            return redirect('/login/')
    print(session)
    return redirect('/login/')    

@login.route('/logout')
def Logout():
    print(session)
    session.clear()
    return redirect('/')