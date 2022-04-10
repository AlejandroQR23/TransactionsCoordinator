"""
Integrantes:
- Lemus Martínez Enrique Joel
- Quijano Ramírez Alejandro
- Reyes Quijano Roberto
"""

from Transaction import Transaction


def main():
    tc = Transaction()
    id = tc.open_transaction()
    print(f"Transaction creada con id: {id}")

    while(True):
        print("\n")
        print(" 1.- cerrar transaccion")
        print(" 2.- abortar transaccion")
        print(" 3.- retiro")
        print(" 4.- deposito")
        print(" 5.- Salir")
        opcion = input(" Introduzca Opcion: ")

        if opcion == '1':
            try:
                tc.close_transaction()
            except Exception as e:
                print(f'\n Error: {e}')
            break

        elif opcion == '2':
            try:
                tc.abort_transaction()
            except Exception as e:
                print(f'\n Error: {e}')
            break

        elif opcion == '3':
            print('\n Retiro')
            withdraw_value = float(input(" Introduzca Cantidad a retirar: "))
            tc.withdraw(withdraw_value)

        elif opcion == '4':
            print('\n Deposito')
            deposit_value = float(input(" Introduzca Cantidad a depositar: "))
            tc.deposit(deposit_value)

        else:
            print('\n opcion no valida')


if __name__ == '__main__':
    main()
