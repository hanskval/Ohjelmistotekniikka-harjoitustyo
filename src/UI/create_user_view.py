import tkinter as tk
from tkinter import messagebox

class CreateUserView:
    def __init__(self, root, user_dao, handle_show_login_view):
        self._root = root
        self._user_dao = user_dao
        self._handle_show_login_view = handle_show_login_view
        
        self._frame = tk.Frame(master=self._root)
        self._initialize()

    def pack(self):
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        tk.Label(master=self._frame, text="Luo uusi käyttäjä", font=("Arial", 14)).pack(pady=10)

        tk.Label(master=self._frame, text="Uusi käyttäjätunnus:").pack()
        self._username_entry = tk.Entry(master=self._frame)
        self._username_entry.pack(pady=5)

        tk.Label(master=self._frame, text="Uusi salasana:").pack()
        self._password_entry = tk.Entry(master=self._frame, show="*")
        self._password_entry.pack(pady=5)

        tk.Button(master=self._frame, text="Luo tunnus", command=self._handle_create_user).pack(pady=10)
        
        # Nappi, joka vie takaisin alkuun
        tk.Button(master=self._frame, text="Takaisin kirjautumiseen", command=self._handle_show_login_view).pack(pady=5)

    def _handle_create_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            messagebox.showerror("Virhe", "Kentät eivät voi olla tyhjiä.")
            return

        existing_user = self._user_dao.find_by_username(username)
        if existing_user:
            messagebox.showerror("Virhe", "Käyttäjätunnus on jo varattu!")
            return

        self._user_dao.create(username, password)
        messagebox.showinfo("Onnistui", f"Käyttäjä {username} luotu! Voit nyt kirjautua sisään.")
        
        # Siirrytään automaattisesti takaisin kirjautumisnäkymään onnistumisen jälkeen
        self._handle_show_login_view()