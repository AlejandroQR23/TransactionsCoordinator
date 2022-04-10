"""
Integrantes:
- Lemus Martínez Enrique Joel
- Quijano Ramírez Alejandro
- Reyes Quijano Roberto
"""


import json


class Transaction:

    transaction_number = 0

    def open_transaction(self) -> str:
        """
        Inicia una transacción y crea un
        identificador único para esta
        """
        f = open('data.json')
        self.data = json.load(f)
        print(self.data)

        self.transaction_number += 1
        return self.transaction_number

    def abort_transaction(self) -> None:
        """
        Cierra la transacción sin que los efectos de sus 
        operaciones sean almacenados en memoria permanente
        """
        pass

    def close_transaction(self) -> None:
        """
        Si la transacción puede ser consumada, almacenará sus resultados en memoria permanente, sino, deberá invocar al método aborta transacción
        """
        pass

    def deposit(self, amount: float) -> None:
        """
        Realiza un deposito a una cuenta bancaria
        """
        pass

    def withdraw(self, amount: float) -> None:
        """
        Realiza un retiro a una cuenta bancaria
        """
        pass
