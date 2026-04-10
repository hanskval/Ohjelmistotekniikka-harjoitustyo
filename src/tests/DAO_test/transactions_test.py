import unittest
from src.DAO.transactionsDAO import TransactionsDAO
from src.database.connection import get_database_connection
from src.database.initialize_database import initialize_database
import src.DAO.userDAO as userDAO


class TestuserDAO(unittest.TestCase):
    def setUp(self):
        # Alustetaan database ennen jokaista testiä
        initialize_database()
        self.connection = get_database_connection()
        self.transactions_dao = TransactionsDAO(self.connection)
        self.users_dao = userDAO.UserDAO(self.connection)
        # Luo käyttäjän tietokantaan
        self.users_dao.create("testuser", "password123")
        user = self.users_dao.find_by_username("testuser")
        user_id = user[0]  # id on index 0
        self.transactions_dao.create(
            user_id=user_id, amount=100.0, category="Salary", description="Monthly salary")

    def test_find_by_user_id(self):
        user = self.users_dao.find_by_username("testuser")
        user_id = user[0]
        transactions = self.transactions_dao.find_by_user_id(user_id)
        self.assertEqual(len(transactions), 1)

    def test_create_transaction(self):
        user = self.users_dao.find_by_username("testuser")
        user_id = user[0]
        self.transactions_dao.create(
            user_id=user_id, amount=-50.0, category="Groceries", description="Weekly groceries")
        transactions = self.transactions_dao.find_by_user_id(user_id)
        self.assertEqual(len(transactions), 2)

    def test_get_balance(self):
        # Oletetaan, että käyttäjällä on
        user = self.users_dao.find_by_username("testuser")
        balance = self.transactions_dao.get_balance(user['id'])
        self.assertEqual(balance, 100.0)
