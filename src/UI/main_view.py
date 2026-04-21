from tkinter import ttk, constants, messagebox

class MainView:
    def __init__(self, root, user_dao, handle_logout, user, transaction_dao, handle_show_transactions):
        self._root = root
        self._user_dao = user_dao
        self._transaction_DAO = transaction_dao
        self._handle_logout = handle_logout
        self._handle_show_transactions = handle_show_transactions
        self._user = user
        self._frame = None

        self._desc_entry = None
        self._category_entry = None
        self._amount_entry = None
        self._balance_label = None
        self._income_label = None
        self._expense_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):

        self._frame.destroy()

    def _handle_add_transaction(self):
            # mitä käyttäjä kirjoitti kenttiin
            description = self._desc_entry.get()
            category = self._category_entry.get()
            amount_str = self._amount_entry.get()

            if not description or not category or not amount_str:
                messagebox.showerror("Virhe", "Täytä kaikki kentät!")
                return

            try:
                # Muuttaa teksti desimaaliluvuksi
                amount = float(amount_str)
                
                # tallentaan tietokantaan
                self._transaction_DAO.create(self._user['id'], amount, category, description)

                self._desc_entry.delete(0, constants.END)
                self._category_entry.delete(0, constants.END)
                self._amount_entry.delete(0, constants.END)

                # päivitetään saldon
                new_balance = self._transaction_DAO.get_balance(self._user['id'])
                new_income = self._transaction_DAO.get_income(self._user['id'])
                new_expenses = self._transaction_DAO.get_expenses(self._user['id'])
                
                self._balance_label.config(text=f"Saldo: {new_balance:.2f} €")
                self._income_label.config(text=f"Tulot: {new_income:.2f} €")
                self._expense_label.config(text=f"Menot: {new_expenses:.2f} €")
                
                balance_color = "green" if new_balance >= 0 else "red"
                self._balance_label.config(text=f"Saldo:\n{new_balance:.2f} €", foreground=balance_color)
                
                messagebox.showinfo("Onnistui", "Tapahtuma lisätty!")

            except ValueError:
                
                messagebox.showerror("Virhe", "Summan pitää olla numero (käytä pistettä erottimena)!")
                
    def _initialize(self):
        username = self._user['username']
        self._frame = ttk.Frame(master=self._root)
        
        current_balance = self._transaction_DAO.get_balance(self._user['id'])
        current_income = self._transaction_DAO.get_income(self._user['id'])
        current_expenses = self._transaction_DAO.get_expenses(self._user['id'])

        title_label = ttk.Label(master=self._frame, text="Budgeting software!")
        welcome_label = ttk.Label(master=self._frame, text=f"Tervetuloa, {username}!")
        
        # tulot ja menot näytetään erivärisinä, jotta ne erottuvat selkeämmin
        summary_frame = ttk.Frame(master=self._frame)
        summary_frame.grid(row=2, column=0, pady=10, sticky=constants.EW)
        
        self._income_label = ttk.Label(master=summary_frame, text=f"Tulot:\n{current_income:.2f} €", foreground="green", font=("Arial", 12, "bold"), justify=constants.CENTER)
        self._income_label.grid(row=0, column=0, padx=20)

        self._expense_label = ttk.Label(master=summary_frame, text=f"Menot:\n{current_expenses:.2f} €", foreground="red", font=("Arial", 12, "bold"), justify=constants.CENTER)
        self._expense_label.grid(row=0, column=1, padx=20)

        balance_color = "green" if current_balance >= 0 else "red"
        self._balance_label = ttk.Label(master=summary_frame, text=f"Saldo:\n{current_balance:.2f} €", foreground=balance_color, font=("Arial", 14, "bold"), justify=constants.CENTER)
        self._balance_label.grid(row=0, column=2, padx=20)
        
        logout_button = ttk.Button(master=self._frame, text="Kirjaudu ulos", command=self._handle_logout)

        title_label.grid(row=0, column=0, padx=10, pady=5)
        welcome_label.grid(row=1, column=0, padx=10, pady=5)
        self._balance_label.grid(row=2, column=0, padx=10, pady=20)
        logout_button.grid(row=3, column=0, padx=10, pady=10)
        history_button = ttk.Button(master=self._frame, text="Näytä tapahtumat", command=lambda: self._handle_show_transactions(self._user))
        history_button.grid(row=3, column=1, padx=10, pady=10)
        
        form_frame = ttk.LabelFrame(master=self._frame, text="Lisää uusi tapahtuma")
        form_frame.grid(row=4, column=0, padx=10, pady=10, sticky=constants.EW)

        ttk.Label(master=form_frame, text="Kuvaus:").grid(row=0, column=0, padx=5, pady=5)
        self._desc_entry = ttk.Entry(master=form_frame)
        self._desc_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(master=form_frame, text="Kategoria:").grid(row=1, column=0, padx=5, pady=5)
        self._category_entry = ttk.Entry(master=form_frame)
        self._category_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(master=form_frame, text="Summa (€) (+/-):").grid(row=2, column=0, padx=5, pady=5)
        self._amount_entry = ttk.Entry(master=form_frame)
        self._amount_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = ttk.Button(
            master=form_frame, 
            text="Tallenna", 
            command=self._handle_add_transaction
        )
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self._frame.columnconfigure(0, weight=1)