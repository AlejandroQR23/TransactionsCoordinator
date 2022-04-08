"""
Integrantes:
- Lemus Martínez (?) Enrique Joel
- Quijano Ramírez Alejandro
- Reyes Quijano Roberto
"""


class TransactionsCoordinator:

    def open_transaction(self) -> str:
        """
        Inicia una transacción y crea un
        identificador único para esta
        """
        pass

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
