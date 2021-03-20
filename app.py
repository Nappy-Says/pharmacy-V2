from datetime import *
from flask import Flask,redirect, render_template
from flask.globals import session
from Blueprints.login import login as loginBlueprint
from Blueprints.client import client as clientBlueprint
from Blueprints.products import products as productsBlueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jUMAISINBA SHEL BEL BEL BEL'
# app.permanent_session_lifetime = datetime


app.register_blueprint(loginBlueprint, url_prefix = '/login')
app.register_blueprint(clientBlueprint, url_prefix = '/client')
app.register_blueprint(productsBlueprint, url_prefix = '/products')


@app.route('/')
def Index():
    if not 'username' in session:
       return redirect('/login') 
    return render_template('index.html')

@app.route('/login')
def RedirecttoLogin():
    return redirect('/login/')

@app.route('/products')
def Show_products():
    return render_template('products.html')

@app.route('/login')
def redirectt():
    return redirect('/login/')
