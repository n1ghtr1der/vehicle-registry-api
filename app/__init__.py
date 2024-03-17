from flask import Flask
from ZODB import FileStorage, DB

app = Flask(__name__)

storage = FileStorage.FileStorage('db/car_registry.fs', read_only=False)
db = DB(storage)
connection = db.open()
app.root = connection.root()

from app import routes