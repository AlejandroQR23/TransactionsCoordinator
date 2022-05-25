from pymongo import MongoClient


def connect_db():
    CONNECTION_STRING = "mongodb+srv://alqr_node:alqr2309@cluster0.imft1.mongodb.net/TransactionsCoordinator"

    client = MongoClient(CONNECTION_STRING)

    db = client['TransactionsCoordinator']
    collection = db['bankData']

    return (db, collection)
