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

    def test_create_user(self):
        self.users_dao.create("testuser", "password123")
        users = self.users_dao.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], "testuser")  # index 1 on username

    def test_find_by_username(self):
        self.users_dao.create("testuser", "password123")
        user = self.users_dao.find_by_username("testuser")
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "testuser")  # index 1 on username
