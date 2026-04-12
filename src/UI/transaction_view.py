from tkinter import ttk, constants, messagebox

class TransactionsView:
    def __init__(self, root, transaction_dao, handle_back, user):
        self._root = root
        self._transaction_DAO = transaction_dao
        self._handle_back = handle_back
        self._user = user
        self._frame = None
        self._tree = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _handle_delete(self):
        # Katsotaan, mikä rivi on valittuna taulukosta
        selected_item = self._tree.selection()
        if not selected_item:
            messagebox.showwarning("Huomio", "Valitse poistettava tapahtuma listalta klikkaamalla sitä!")
            return

        # Haetaan valitun rivin tiedot
        item_values = self._tree.item(selected_item[0])['values']
        transaction_id = item_values[0] 

        # Varmistetaan käyttäjältä, ettei tule vahinkopoistoja
        if messagebox.askyesno("Vahvistus", "Haluatko varmasti poistaa tämän tapahtuman?"):
            self._transaction_DAO.delete(transaction_id)
            self._refresh_list() # päivitetään lista poiston jälkeen
            messagebox.showinfo("Onnistui", "Tapahtuma poistettu.")

    def _refresh_list(self):
        # Tyhjennetään vanha lista
        for item in self._tree.get_children():
            self._tree.delete(item)
        
        # Haetaan databasesta uudet tiedot ja lisätään taulukkoon
        transactions = self._transaction_DAO.find_by_user_id(self._user['id'])
        for t in transactions:
            # Timestampista otetaan vain 10 ensimmäistä merkkiä (esim. 2024-03-15)
            date_str = t['timestamp'][:10] if t['timestamp'] else "-"
            self._tree.insert("", constants.END, values=(t['id'], date_str, t['description'], t['category'], f"{t['amount']:.2f} €"))

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        ttk.Label(master=self._frame, text="Kaikki tapahtumat", font=("Arial", 16, "bold")).pack(pady=10)

        # luodaan taulukko tapahtumille
        columns = ("id", "date", "desc", "cat", "amount")
        self._tree = ttk.Treeview(master=self._frame, columns=columns, show="headings", height=15)
        
        # otiskot
        self._tree.heading("id", text="ID")
        self._tree.column("id", width=30)
        self._tree.heading("date", text="Päivämäärä")
        self._tree.heading("desc", text="Kuvaus")
        self._tree.heading("cat", text="Kategoria")
        self._tree.heading("amount", text="Summa")

        self._tree.pack(fill=constants.BOTH, expand=True, padx=10, pady=5)

        self._refresh_list()

        button_frame = ttk.Frame(master=self._frame)
        button_frame.pack(fill=constants.X, padx=10, pady=10)

        ttk.Button(master=button_frame, text="Poista valittu", command=self._handle_delete).pack(side=constants.LEFT)
        ttk.Button(master=button_frame, text="Takaisin päänäkymään", command=self._handle_back).pack(side=constants.RIGHT)