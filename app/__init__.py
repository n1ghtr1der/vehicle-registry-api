from flask import Flask
import ZODB, ZODB.FileStorage, ZODB.DB

app = Flask(__name__)

storage = ZODB.FileStorage.FileStorage('car_registry.fs')
db = ZODB.DB(storage)
connection = db.open()
app.root = connection.root()

from app import routes