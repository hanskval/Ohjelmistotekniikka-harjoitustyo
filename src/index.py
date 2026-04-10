import tkinter as tk
from src.database.connection import get_database_connection
from src.DAO.userDAO import UserDAO
from src.DAO.transactionsDAO import TransactionsDAO
from src.UI.ui import UI     # Olettaen, että UI on tässä tiedostossa

def main():

    # 1. Alustetaan tietokantayhteys
    connection = get_database_connection()

    # 2. Luodaan DAO ja annetaan sille yhteys
    user_dao = UserDAO(connection)
    transaction_dao = TransactionsDAO(connection)

    # 3. Luodaan Tkinter-pääikkuna
    window = tk.Tk()

    # 4. Luodaan kirjautumisnäkymä ja annetaan sille ikkuna sekä DAO
    ui = UI(window, user_dao, transaction_dao)

    ui.start()

    # 5. Käynnistetään sovellus
    window.mainloop()


if __name__ == "__main__":
    main()
