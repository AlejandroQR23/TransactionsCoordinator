"""
Integrantes:
- Lemus Martínez Enrique Joel
- Quijano Ramírez Alejandro
- Reyes Quijano Roberto
"""

from Transaction import Transaction


def main():
    tc = Transaction()
    transaction_id = tc.open_transaction()
    print(f"ID de la transacción: {transaction_id}")

    tc.withdraw(10)
    tc.deposit(100)
    try:
        tc.close_transaction()
        tc.abort_transaction()
    except Exception as e:
        print(f"Transaccion abortada: {e}")


if __name__ == "__main__":
    main()
