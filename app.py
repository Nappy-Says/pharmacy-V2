from datetime import *
from flask import Flask,redirect, render_template
from flask.globals import session
from Blueprints.login import login as loginBlueprint
from Blueprints.client import client as clientBlueprint
from Blueprints.products import products as productsBlueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jUMAISINBA SHEL BEL BEL BEL'
# app.permanent_session_lifetime = datetime


app.register_blueprint(loginBlueprint, url_prefix = '/login', template_folder='templates/login')
app.register_blueprint(clientBlueprint, url_prefix = '/client')
app.register_blueprint(productsBlueprint, url_prefix = '/products', template_folder='templates/products')


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
    if not 'username' in session:
       return redirect('/login') 
    return redirect('/products/')

@app.route('/client')
def show_client():
    if not 'username' in session:
       return redirect('/login') 
    return redirect('/client/')