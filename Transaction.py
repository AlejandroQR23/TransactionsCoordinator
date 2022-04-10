import json

FILE_URL = 'data/accounts.json'


class Transaction:

    transaction_number = 0

    def __init__(self):
        self.hasError = False
        self.transaction_number += 1

    def open_transaction(self) -> str:
        """
        Inicia una transacción y crea un
        identificador único para esta.

        Lee los datos de la memoria permanente.
        """
        f = open(FILE_URL)
        self.data = json.load(f)

        self.balance = self.data['account']['balance']

        return self.transaction_number

    def abort_transaction(self) -> None:
        """
        Cierra la transacción sin que los efectos de sus 
        operaciones sean almacenados en memoria permanente.

        Notifica al usuario que se ha abortado la transacción por medio
        de un mensaje en una excepción.
        """
        raise Exception(f"Transaccion {self.transaction_number} abortada")

    def close_transaction(self) -> None:
        """
        Si la transacción puede ser consumada, almacenará sus resultados en memoria permanente, sino aborta la transacción
        """
        if(self.hasError):
            self.abort_transaction()
        else:
            with open(FILE_URL, "w") as outfile:
                json.dump(self.data, outfile)

    def deposit(self, amount: float) -> None:
        """
        Realiza un deposito a una cuenta bancaria

        Parametros:
        amount: un flotante con la cantidad a depositar
        """
        self.balance += amount
        self.data['account']['balance'] = self.balance

    def withdraw(self, amount: float) -> bool:
        """
        Realiza un retiro a una cuenta bancaria

        Parametros:
        amount: un flotante con la cantidad a retirar

        Regresa:
        Un booleano indicando si el retiro se puede hacer
        """
        if amount > self.balance:
            return False

        self.balance -= amount
        self.data['account']['balance'] = self.balance

        return True
