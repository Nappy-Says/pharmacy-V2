from flask import Blueprint, session, render_template, request, redirect
from models import *
import os


path = 'D:/project/pharmacy-V2/static/images/products/'
products = Blueprint('products', __name__)

@products.route('/add', methods = ['GET'])
def products_add():
    return render_template('product_add.html')


@products.route('/add', methods = ['POST'])
def product_create():
    _name = request.form.get('name')
    _barcode = request.form.get('barcode')
    _select1 = request.form.get('select1')
    _select2 = request.form.get('select2')
    _file = request.files['file']
    _file.save(path + '1.png')
    name = 'products/1.png'
    p = Products(name = _name, barcode = _barcode, file = name).save()
    return 'ДОБАВЛЕНО'


@products.route('/',methods = ['GET'])
def Show_products():
    data = Products.select()
    return render_template('products.html', data=data)

@products.route('/buy', methods = ['GET'])
def product_buy():
    return render_template('products_buy.html')

@products.route('/dimension', methods = ['GET'])
def products_dimension():
    return render_template('products_dimension.html')

@products.route('/category', methods = ['GET'])
def products_category():
    return render_template('products_category.html')