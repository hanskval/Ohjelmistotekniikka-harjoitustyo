import sqlite3
from .connection import get_database_connection


def drop_tables():
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS transactions;")
        cursor.execute("DROP TABLE IF EXISTS users;")


def create_tables():
    with get_database_connection() as connection:
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash BLOB NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT,
                description TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );
        ''')


def initialize_database():
    try:
        drop_tables()
        create_tables()
        print("Tietokanta alustettu onnistuneesti!")

    except sqlite3.Error as e:
        print(f"Virhe tietokannan alustuksessa: {e}")
