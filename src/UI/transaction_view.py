import tkinter as tk
from tkinter import ttk, constants, messagebox

class TransactionsView:
    """ Näkymä joka näyttää käyttäjälle kaikki tämänhetkiset tapahtumat taulukkomuodossa 
    ja tarjoaa mahdollisuuden poistaa tapahtumia """
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
        """ Poistaa valitun tapahtuman tietokannasta ja päivittää listan """
        selected_item = self._tree.selection()
        if not selected_item:
            messagebox.showwarning("Huomio", "Valitse poistettava tapahtuma listalta klikkaamalla sitä!")
            return

        item_values = self._tree.item(selected_item[0])['values']
        transaction_id = item_values[0] 

        if messagebox.askyesno("Vahvistus", "Haluatko varmasti poistaa tämän tapahtuman?"):
            self._transaction_DAO.delete(transaction_id)
            self._refresh_list()
            messagebox.showinfo("Onnistui", "Tapahtuma poistettu.")
    
    def _handle_edit(self):
        """ Hakee valitun tapahtuman tiedot ja avaa muokkausikkunan """
        selected_item = self._tree.selection()
        if not selected_item:
            messagebox.showwarning("Huomio", "Valitse muokattava tapahtuma listalta klikkaamalla sitä!")
            return

        item_values = self._tree.item(selected_item[0])['values']
        self._open_edit_popup(item_values)
        
    def _open_edit_popup(self, item_values):
        """ Rakentaa ponnahdusikkunan valitun tapahtuman muokkausta varten """
        t_id = item_values[0]
        t_desc = item_values[2]
        t_cat = item_values[3]
        t_amount_str = item_values[4]

        popup = tk.Toplevel(self._root)
        popup.title("Muokkaa tapahtumaa")
        popup.geometry("300x250")
        popup.grab_set()

        ttk.Label(popup, text="Kuvaus:").pack(pady=(10, 0))
        desc_var = tk.StringVar(value=t_desc)
        ttk.Entry(popup, textvariable=desc_var).pack()

        ttk.Label(popup, text="Kategoria:").pack(pady=(10, 0))
        cat_var = tk.StringVar(value=t_cat)
        ttk.Entry(popup, textvariable=cat_var).pack()

        clean_amount = str(t_amount_str).replace(" €", "").replace(",", ".")
        ttk.Label(popup, text="Summa (€):").pack(pady=(10, 0))
        amount_var = tk.StringVar(value=clean_amount)
        ttk.Entry(popup, textvariable=amount_var).pack()

        def save_changes():
            new_desc = desc_var.get()
            new_cat = cat_var.get()
            
            try:
                new_amount = float(amount_var.get())
            except ValueError:
                messagebox.showerror("Virhe", "Summan täytyy olla numero!", parent=popup)
                return

            try:
                self._transaction_DAO.update(t_id, new_amount, new_cat, new_desc)
                self._refresh_list()
                popup.destroy()
                messagebox.showinfo("Onnistui", "Tapahtuma päivitetty!")
            except Exception as e:
                messagebox.showerror("Virhe", f"Tallennus epäonnistui: {e}", parent=popup)

        btn_frame = ttk.Frame(popup)
        btn_frame.pack(pady=20)
        ttk.Button(btn_frame, text="Tallenna", command=save_changes).pack(side=constants.LEFT, padx=5)
        ttk.Button(btn_frame, text="Peruuta", command=popup.destroy).pack(side=constants.LEFT, padx=5)
    
    def _refresh_list(self):
        """ Tyhjentää taulukon ja hakee databasesta uudet tapahtumat, jotka näytetään taulukossa """
        for item in self._tree.get_children():
            self._tree.delete(item)

        transactions = self._transaction_DAO.find_by_user_id(self._user['id'])
        for t in transactions:

            date_str = t['timestamp'][:10] if t['timestamp'] else "-"
            self._tree.insert("", constants.END, values=(t['id'], date_str, t['description'], t['category'], f"{t['amount']:.2f} €"))

    def _initialize(self):
        """ Toteuttaa tapahtumien listausnäkymän, joka näyttää käyttäjään 
        liittyviä tapahtumia taulukkomuodossa ja tarjoaa mahdollisuuden poistaa tapahtumia """
        self._frame = ttk.Frame(master=self._root)

        ttk.Label(master=self._frame, text="Kaikki tapahtumat", font=("Arial", 16, "bold")).pack(pady=10)

        columns = ("id", "date", "desc", "cat", "amount")
        self._tree = ttk.Treeview(master=self._frame, columns=columns, show="headings", height=15)
        

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

        ttk.Button(master=button_frame, text="Muokkaa valittua", command=self._handle_edit).pack(side=constants.LEFT, padx=(0, 5))

        ttk.Button(master=button_frame, text="Poista valittu", command=self._handle_delete).pack(side=constants.LEFT)
        ttk.Button(master=button_frame, text="Takaisin päänäkymään", command=self._handle_back).pack(side=constants.RIGHT)
