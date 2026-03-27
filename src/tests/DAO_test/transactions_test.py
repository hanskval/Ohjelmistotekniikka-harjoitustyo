import unittest
from src.DAO.transactionsDAO import TransactionsDAO
from src.database.connection import get_database_connection
from src.database.initialize_database import initialize_database
import src.DAO.userDAO as userDAO

class TestuserDAO(unittest.TestCase):
    def setUp(self):
        # Alustetaan tietokanta ennen jokaista testiä
        initialize_database()
        self.connection = get_database_connection()
        self.transactions_dao = TransactionsDAO(self.connection)
        self.users_dao = userDAO.UserDAO(self.connection)
        self.users_dao.create("testuser", "password123") # Luo käyttäjän tietokantaan
        id = self.users_dao.find_by_username("testuser")['id']
        self.transactions_dao.create(user_id=id, amount=100.0, category="Salary", description="Monthly salary")
        

    def test_get_balance(self):
        # Oletetaan, että käyttäjällä on
        user = self.users_dao.find_by_username("testuser")
        balance = self.transactions_dao.get_balance(user['id'])
        self.assertEqual(balance, 100.0)