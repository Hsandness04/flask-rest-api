import sqlite3
from multiprocessing import connection
from db import db


class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') # One to Many relationship with the ItemModel

    def __init__(self, name, _id):
        self.name = name
        self.store_id = _id # Could cause an error.

    def json(self):
        # Added id, could cause an error.
        return {'name': self.name, 'store_id': self.store_id, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name = ?

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.commit()