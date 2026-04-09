import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(self, root, user_dao, handle_show_create_user_view, handle_show_main_view):
        self._root = root
        self._user_dao = user_dao
        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_show_main_view = handle_show_main_view
        self._frame = tk.Frame(master=self._root)

        self._initialize()

    def pack(self):

        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        # Tuhoaa tämän näkymän
        self._frame.destroy()

    def _initialize(self):

        tk.Label(master=self._frame, text="Kirjaudu sisään",
                 font=("Arial", 14)).pack(pady=10)

        tk.Label(master=self._frame, text="Käyttäjätunnus:").pack()
        self._username_entry = tk.Entry(master=self._frame)
        self._username_entry.pack(pady=5)

        tk.Label(master=self._frame, text="Salasana:").pack()
        self._password_entry = tk.Entry(master=self._frame, show="*")
        self._password_entry.pack(pady=5)

        tk.Button(master=self._frame, text="Kirjaudu",
                  command=self._handle_login).pack(pady=10)

        tk.Button(master=self._frame, text="Luo uusi käyttäjä",
                  command=self._handle_show_create_user_view).pack(pady=5)

    def _handle_login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        user = self._user_dao.find_by_username(username)

        if user and user['password_hash'] == password:
            messagebox.showinfo("Onnistui", f"Tervetuloa sisään, {username}!")
            self._handle_show_main_view(user)
        else:
            messagebox.showerror("Virhe", "Väärä käyttäjätunnus tai salasana.")
