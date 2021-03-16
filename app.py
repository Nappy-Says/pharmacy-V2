from flask import Flask
from Blueprints.login import login as loginBlueprint


app = Flask(__name__)
app.register_blueprint(loginBlueprint, url_prefix = '/login')



@app.route('/login')
def RedirecttoLogin():
    return redirect('/login/')