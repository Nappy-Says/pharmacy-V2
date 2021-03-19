from peewee import *

db = SqliteDatabase('db.db')

class BaseModel(Model):
    class Meta:
        database = db


#Пользователь 
class User(BaseModel):
    id = AutoField()
    fio = CharField()
    login = CharField()
    password = CharField()
    role = CharField()
    status = BooleanField()
    
# Аптека  
class Pharmacy(BaseModel):
    id = AutoField()
    name = CharField()
    address = CharField()
    proceeds = CharField()
    cashier = CharField()
    storage = CharField()

#склад 
class Storage(BaseModel):
    id= AutoField()
    name= CharField()
    pharmacy = ForeignKeyField(Pharmacy, related_name="Pharmacy")

# Поставщики 
# Номера начинаются с +
class Suppliers(BaseModel):
    id = AutoField()
    name = CharField()
    phone = CharField()
    email = CharField()
    coming = FloatField()
    pay = FloatField()
    balance = FloatField()
    description = CharField()

# Клиенты 
class Client(BaseModel):
    id= AutoField()
    fio = CharField()
    phone = IntegerField()
    description = CharField()
    type_client = CharField()
    debit = FloatField()
    credit = FloatField()
    balance = FloatField()
    address = CharField()

# Товары 
class Products(BaseModel):
    id = AutoField()
    barcode = IntegerField()
    name  = CharField()
    file = CharField()

# Закуп товара 
class Buy(BaseModel):
    id = AutoField()
    product = ForeignKeyField(Products, related_name= "Products")
    amount = IntegerField()
    before_price = FloatField()
    after_price = FloatField()
    expiry_date = DateTimeField()

Products.create_table()