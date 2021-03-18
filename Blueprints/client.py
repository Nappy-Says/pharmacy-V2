from flask import Blueprint, render_template, request, redirect
from models import *

client = Blueprint('client', __name__)

@client.route('/add', methods = ['GET'])
def Client_Add():
    return render_template('client.html')
