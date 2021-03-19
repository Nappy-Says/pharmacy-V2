from flask import Blueprint, session, render_template, request, redirect
from models import *

supp = Blueprint('supp', __name__)

@supp.route('/add', methods = ['GET'])
def supp_add():
    return render_template('product_add.html')


@supp.route('/buy', methods = ['GET'])
def supp_manage():
    return render_template('products_buy.html')