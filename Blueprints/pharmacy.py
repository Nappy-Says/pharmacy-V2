from flask import Blueprint, render_template, request, redirect
from models import Client

client = Blueprint('client', __name__)

@client.route('/', methods = ['GET'])
def Show_Manage():
    data = Client.select()
    return render_template('client.html', data=data, length=len(data))

@client.route('/add', methods = ['GET'])
def Client_Add():
    return render_template('client_add.html')

@client.route('/add', methods = ['POST'])
def product_create():
    _fio = request.form.get('fio')
    _type_client = request.form.get('type_select')
    _phone= request.form.get('phone')
    _email = request.form.get('email')
    _descrition = request.form.get("description")
    _phar_select = request.form.get("select_pharmacy")
    cl = Client(fio = _fio, type_client = _type_client, phone = _phone, email = _email, description = _descrition, balance  = 0).save()
    return redirect('/client')

@client.route('/edit/<id>', methods = ['POST'])
def product_edit(id):
    cl = Client.get(Client.id == id)
    cl.fio = request.form.get('fio')
    cl.type_client = request.form.get('type_select')
    cl.phone= request.form.get('phone')
    cl.email = request.form.get('email')
    cl.descrition = request.form.get("description")
    cl.phar_select = request.form.get("select_pharmacy")
    cl.save()
    return redirect('/client')


@client.route('/edit/<id>')
def Editclient(id):
    cl = Client.get(Client.id == id)
    return render_template('client_edit.html', client = cl)


@client.route('/delete/<id>')
def DeleteClient(id):
    cl = Client.get(Client.id == id)
    cl.delete_instance()
    return redirect('/client')
