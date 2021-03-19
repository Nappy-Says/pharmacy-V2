from peewee import *

db = SqliteDatabase('db.db')

class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    id = AutoField()
    username = CharField()
    password = CharField()


