class UserDAO:
    def __init__(self, connection):
        self._connection = connection

    def create(self, username, password_hash):
        """ Toteuttaa käyttäjän luomisen tietokantaan """
        cursor = self._connection.cursor()
        cursor.execute('''
            INSERT INTO users (username, password_hash) VALUES (?, ?)''',
                       (username, password_hash)
                       )
        self._connection.commit()

    def find_by_username(self, username):
        """ Toteuttaa käyttäjän haun käyttäjänimen perusteella """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()

        return row if row else None

    def find_all(self):
        """ Toteuttaa kaikkien käyttäjien haku tietokannasta """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        row = cursor.fetchall()

        return row if row else None
