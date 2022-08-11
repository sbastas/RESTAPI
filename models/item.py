import sqlite3
from db import database

class ItemModel(database.Model):
    
    __tablename__ = 'items'

    id = database.Column(database.Integer, primary_key=True)
    name =database.Column(database.String(80))
    price = database.Column(database.Float(precision=2))

    store_id = database.Column(database.Integer, database.ForeignKey('stores.id'))
    store = database.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    def delete_from_db(self):
        database.session.delete(self)
        database.session.commit()