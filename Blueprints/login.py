from flask import Blueprint, session, render_template, request
from models import *

login = Blueprint('login', __name__)

def CheckAuth():
    if 'username' in session:
        return redirect('/')

@login.route('/', methods = ['GET'])
def SendHtmlLogin():
    CheckAuth()

    return render_template('login.html')

@login.route('/', methods = ['POST'])
def CheckLogin():
    _username = request.form['username']
    _password = request.form['password']

    return _username + ' ' + _password