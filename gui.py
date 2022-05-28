import tkinter as tk
from tkinter import messagebox

from models.Account import Accounts
from Transaction import Transaction


class BankApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Datos de la cuenta
        self.db = Accounts()
        self.__account = None

        # Transacciones
        self.transaction = Transaction()

        # Ventanas
        self._frame = None
        self.set_up()
        self.switch_frame(StartPage)

    def set_up(self):
        """
        Configura la ventana inicial.
        """
        self.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.geometry("350x250")

    def __on_closing(self):
        """
        Maneja el cierre de la aplicacion asegurando que los permisos para
        el manejo de la cuenta sean desbloqueados y la transaccion en curso (si la hay) se aborte.
        """
        if messagebox.askokcancel("Salir", "¿Seguro que deseas salir? Los cambios no se reflejaran en tu cuenta"):
            if self.__account:
                self.end_transaction(error=True)
            self.destroy()

    def switch_frame(self, frame_class):
        """
        Elimina el frame actual y lo reemplaza con uno nuevo.
        """
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def show_error(self, message: str, frame: tk.Frame):
        """
        Despliega una ventana de error y envia
        al usuario a una ventana especificada (frame).
        """
        messagebox.showerror(title="Error", message=message)
        self.switch_frame(frame)

    def show_info(self, message: str, frame: tk.Frame):
        """
        Despliega una ventana de informacion y envia
        al usuario a una ventana especificada (frame).
        """
        messagebox.showinfo(title="Info", message=message)
        self.switch_frame(frame)

    def select_account(self, selected_account: str):
        """
        Busca una cuenta en la base de datos a partir
        del nombre de cuenta dado por el usuario.

        Si la cuenta existe, cambia a la ventana de Menu y abre una
        nueva transaccion para hacer operaciones en ella.
        """
        if len(selected_account) > 0:
            self.__account = self.db.select_account(selected_account)
            self.validate_account()
        else:
            self.show_error("No ha seleccionado una cuenta", StartPage)

    def validate_account(self):
        """
        Valida que se haya seleccionado una cuenta valida
        al buscarla en la base de datos. Si la cuenta existe, verifica
        tambien si se encuentra disponible.

        Si la cuenta existe y está disponible, bloquea sus permisos y abre una transacción nueva
        para realizar operaciones sobre esa cuenta.
        """
        if not self.__account:
            self.show_error("Seleccione una cuenta valida", StartPage)
        if not self.get_account_availability():
            self.show_error(
                "La cuenta seleccionada esta ocupada en este momento", StartPage)
        else:
            self.db.lock_account()
            self.transaction.open_transaction(self.__account)
            self.switch_frame(MenuPage)

    def end_transaction(self, error=False):
        """
        Termina la transacción. Si hay un error, la transacción es abortada.
        En otro caso se termina la transacción y sus datos temporales son guardados
        en la base de datos para luego desbloquear los permisos de la cuenta.
        """
        if error:
            self.show_info("Transaccion abortada", StartPage)
        else:
            balance = self.transaction.close_transaction()
            self.db.update_balance(balance)
            self.show_info("Transaccion exitosa", StartPage)
        self.db.unlock_account()

    def deposit(self, amount: str):
        """
        Realiza un deposito a una cuenta bancaria
        """
        self.transaction.deposit(int(amount))
        self.end_transaction()

    def withdraw(self, amount: str):
        """
        Realiza un retiro a una cuenta bancaria.
        Si no se pudo efectuar el retiro por fondos insuficientes la operacion
        no se realiza y en su lugar se arroja un mensaje de error.
        """
        if self.transaction.withdraw(int(amount)):
            self.end_transaction()
        else:
            self.show_error("Fondos insuficientes", WithdrawPage)

    def get_account_name(self):
        return self.__account["accountName"]

    def get_account_balance(self):
        return str(self.__account["balance"])

    def get_account_availability(self):
        return self.__account["isAvailable"]


class StartPage(tk.Frame):
    """
    Ventana inicial que contiene los datos del equipo.
    En esta se selecciona la cuenta sobre la que se desea operar.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Coordinador de Transacciones")
        tk.Label(self, text="Integrantes: \nLemus Martinez Enrique Joel\nQuijano Ramirez Luis Alejandro\nReyes Quijano Roberto").pack(
            side="top", fill="x", pady=10)
        text_box = tk.Entry(self, font="Helvetica 15")
        text_box.pack(fill="x", pady=5, padx=5)

        tk.Button(self, text="Seleccionar cuenta",
                  command=lambda: master.select_account(text_box.get())).pack(padx=5, pady=5)


class MenuPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Menu")
        tk.Label(self, text=master.get_account_name(), font="Helvetica 15").pack(
            side="top", fill="x", pady=5, padx=5)

        tk.Button(self, text="Depositar",
                  command=lambda: master.switch_frame(DepositPage)).pack(padx=5, pady=5)
        tk.Button(self, text="Retirar",
                  command=lambda: master.switch_frame(WithdrawPage)).pack(padx=5, pady=5)
        tk.Button(self, text="Consultar balance",
                  command=lambda: master.switch_frame(BalancePage)).pack(padx=5, pady=5)
        tk.Button(self, text="Cerrar transacción",
                  command=lambda: master.switch_frame(StartPage)).pack(padx=5, pady=5)


class BalancePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Consultar saldo")
        tk.Label(self, text="Cuenta: " + master.get_account_name(),
                 font="Arial 20").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Balance: " + master.get_account_balance(),
                 font="Arial 16").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Regresar al menu",
                  command=lambda: master.switch_frame(MenuPage)).pack(padx=5, pady=(45, 5))


class DepositPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Depositar")
        tk.Label(self, text="Cuenta: " + master.get_account_name(),
                 font="Arial 20").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Balance: " + master.get_account_balance(),
                 font="Arial 16").pack(side="top", fill="x", pady=5)

        amount_entry = tk.Entry(self, font="Helvetica 15")
        amount_entry.pack(fill="x", padx=5, pady=5)

        tk.Button(self, text="Realizar deposito",
                  command=lambda: master.deposit(amount_entry.get())).pack(padx=5, pady=(45, 5))
        tk.Button(self, text="Regresar al menu",
                  command=lambda: master.switch_frame(MenuPage)).pack(padx=5, pady=5)


class WithdrawPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Retirar")
        tk.Label(self, text="Cuenta: " + master.get_account_name(),
                 font="Arial 20").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Balance: " + master.get_account_balance(),
                 font="Arial 16").pack(side="top", fill="x", pady=5)

        amount_entry = tk.Entry(self, font="Helvetica 15")
        amount_entry.pack(fill="x", padx=5, pady=5)

        tk.Button(self, text="Realizar retiro",
                  command=lambda: master.withdraw(amount_entry.get())).pack(padx=5, pady=(45, 5))
        tk.Button(self, text="Regresar al menu",
                  command=lambda: master.switch_frame(MenuPage)).pack(padx=5, pady=5)


if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
