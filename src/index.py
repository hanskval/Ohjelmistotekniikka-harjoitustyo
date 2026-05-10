import tkinter as tk
from src.database.connection import get_database_connection
from src.DAO.userDAO import UserDAO
from src.DAO.transactionsDAO import TransactionsDAO
from src.UI.ui import UI

def main():


    connection = get_database_connection()


    user_dao = UserDAO(connection)
    transaction_dao = TransactionsDAO(connection)

    window = tk.Tk()

    ui = UI(window, user_dao, transaction_dao)

    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
