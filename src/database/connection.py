import sqlite3
import os
from src.config import DATABASE_PATH


def get_database_connection():
    # Varmistetaan, että tietokantahakemisto on olemassa
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    # Kytketään viiteavainten valvonta päälle
    connection.execute("PRAGMA foreign_keys = ON;")

    return connection
