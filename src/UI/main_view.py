from tkinter import ttk, constants

class MainView:
    def __init__(self, root, user_dao, handle_logout, user, transaction_dao):
        self._root = root
        self._user_dao = user_dao
        self._transaction_DAO = transaction_dao
        self._handle_logout = handle_logout
        self._user = user
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):

        self._frame.destroy()

    def _initialize(self):
        username = self._user['username']
        self._frame = ttk.Frame(master=self._root)
        current_balance = self._transaction_DAO.get_balance(self._user['id'])

        label = ttk.Label(
            master=self._frame, 
            text="Budgeting software!"
        )
        label = ttk.Label(
            master=self._frame, 
            text=f"Tervetuloa, {username}!"
        )
        
        self._balance_label = ttk.Label(
            master=self._frame,
            text=f"Saldo: {current_balance:.2f} €",
            font=("Arial", 16, "bold")
        )
        self._balance_label.grid(row=2, column=0, padx=10, pady=20)

        # kirjaudu ulos
        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._handle_logout
        )

        label.grid(row=0, column=0, padx=10, pady=10)
        logout_button.grid(row=1, column=0, padx=10, pady=10)


        self._frame.columnconfigure(0, weight=1)
