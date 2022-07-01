from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from pkg_resources import require
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Itemlist
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'hunter'
api = Api(app)


jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') 
api.add_resource(Itemlist, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')

