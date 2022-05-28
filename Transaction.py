class Transaction:

    transaction_number = 0

    def __init__(self):
        self.has_error = False
        self.transaction_number += 1

    def open_transaction(self, data: dict) -> int:
        """
        Inicia una transacción y crea un
        identificador único para esta.

        Establece el balance a partir de los datos
        extraidos de la bd. 
        """
        self.balance = data['balance']

        return self.transaction_number

    def abort_transaction(self) -> None:
        """
        Cierra la transacción sin que los efectos de sus 
        operaciones sean almacenados en memoria permanente.

        Notifica al usuario que se ha abortado la transacción por medio
        de un mensaje en una excepción.
        """
        raise Exception(f"Transaccion {self.transaction_number} abortada")

    def close_transaction(self) -> int:
        """
        Si la transacción puede ser consumada, regresa el balance 
        temporal para ser almacenado en la base de datos
        """
        if(self.has_error):
            self.abort_transaction()
        else:
            return self.balance

    def deposit(self, amount: int) -> None:
        """
        Realiza un deposito a una cuenta bancaria

        Parametros:
        amount: un entero con la cantidad a depositar
        """
        self.balance += amount

    def withdraw(self, amount: int) -> bool:
        """
        Realiza un retiro a una cuenta bancaria

        Parametros:
        amount: un entero con la cantidad a retirar

        Regresa:
        Un booleano indicando si el retiro se puede hacer
        """
        if amount > self.balance:
            return False

        self.balance -= amount

        return True
