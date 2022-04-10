import json


class Transaction:

    transaction_number = 0

    def __init__(self):
        self.hasError = False
        self.transaction_number += 1

    def open_transaction(self) -> str:
        """
        Inicia una transacción y crea un
        identificador único para esta
        """
        f = open('data/accounts.json')
        data = json.load(f)

        self.balance = data['account']['balance']

        return self.transaction_number

    def abort_transaction(self) -> None:
        """
        Cierra la transacción sin que los efectos de sus 
        operaciones sean almacenados en memoria permanente
        """
        raise Exception("Transaccion abortada")

    def close_transaction(self) -> None:
        """
        Si la transacción puede ser consumada, almacenará sus resultados en memoria permanente, sino, deberá invocar al método aborta transacción
        """
        pass

    def deposit(self, amount: float) -> None:
        """
        Realiza un deposito a una cuenta bancaria
        """
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Realiza un retiro a una cuenta bancaria

        Regresa: Un booleano indicando si el retiro se puede hacer
        """
        if amount > self.balance:
            return False
        self.balance -= amount
        return True
