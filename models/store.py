from db import database

class StoreModel(database.Model):
    
    __tablename__ = 'stores'

    id = database.Column(database.Integer, primary_key=True)
    name =database.Column(database.String(80))

    items = database.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    def delete_from_db(self):
        database.session.delete(self)
        database.session.commit()