from flask import Flask,redirect, render_template
from Blueprints.login import login as loginBlueprint


app = Flask(__name__)
app.register_blueprint(loginBlueprint, url_prefix = '/login')


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/login')
def RedirecttoLogin():
    return redirect('/login/')

