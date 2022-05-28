from pymongo import MongoClient

CONNECTION_STRING = ""


class Accounts:
    def __init__(self):
        self.__connect_db()

    def __connect_db(self):
        """
        Inicia la conexion a la base de datos y enlaza
        con la tabla de cuentas en esta.
        """
        try:
            client = MongoClient(CONNECTION_STRING)
        except:
            print("No se pudo conectar a la base de datos")

        self.__db = client['TransactionsCoordinator']
        self.__collection = self.__db['BankData']

    def select_account(self, account_name: str):
        """
        Busca una cuenta en la tabla de cuentas de la bd
        usando el nombre de esta como parametro de busqueda
        y regresa la primera coincidencia.
        """
        self.queryByName = {"accountName": account_name}
        return self.__collection.find_one(self.queryByName)

    def update_balance(self, balance: int):
        updated_account = {"$set": {"balance": balance}}
        self.__collection.update_one(self.queryByName, updated_account)

    def lock_account(self):
        updated_account = {"$set": {"isAvailable": False}}
        self.__collection.update_one(self.queryByName, updated_account)

    def unlock_account(self):
        updated_account = {"$set": {"isAvailable": True}}
        self.__collection.update_one(self.queryByName, updated_account)
