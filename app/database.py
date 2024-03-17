from ZODB import FileStorage, DB

def init_database():
    storage = FileStorage.FileStorage('db/car_registry.fs')
    db = DB(storage)
    connection = db.open()
    root = connection.root()
    return root, connection, db

def close_connection(db, connection):
    connection.close()
    db.close()