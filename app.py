from flask import Flask,redirect, render_template
from Blueprints.login import login as loginBlueprint
from Blueprints.client import client as clientBlueprint
from Blueprints.products import products as productsBlueprint
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.register_blueprint(loginBlueprint, url_prefix = '/login')
app.register_blueprint(clientBlueprint, url_prefix = '/client')
app.register_blueprint(productsBlueprint, url_prefix = '/products')
bootstrap = Bootstrap(app)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/login')
def RedirecttoLogin():
    return redirect('/login/')

@app.route('/products')
def Show_products():
    return render_template('products.html')

