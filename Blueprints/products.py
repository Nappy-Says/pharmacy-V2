from flask import Blueprint, session, render_template, request, redirect
from models import *

products = Blueprint('products', __name__)

@products.route('/add', methods = ['GET'])
def products_add():
    return render_template('product_add.html')

@products.route('/buy', methods = ['GET'])
def product_buy():
    return render_template('products_buy.html')

@products.route('/dimension', methods = ['GET'])
def products_dimension():
    return render_template('products_dimension.html')

@products.route('/category', methods = ['GET'])
def products_category():
    return render_template('products_category.html')