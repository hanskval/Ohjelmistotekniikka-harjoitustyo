import unittest
from src.DAO.userDAO import UserDAO
from src.database.connection import get_database_connection
from src.database.initialize_database import initialize_database

class TestuserDAO(unittest.TestCase):
    
    def setUp(self):
        # Alustetaan tietokanta ennen jokaista testiä
        initialize_database()
        self.connection = get_database_connection()
        self.users_dao = UserDAO(self.connection)
        self.users_dao.create("testuser", "password123") # Luo käyttäjän tietokantaan
    
    def test_find_by_username(self):
        user = self.users_dao.find_by_username("testuser")
        self.assertIsNotNone(user)
        self.assertEqual(user['username'], "testuser")