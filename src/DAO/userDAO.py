class UserDAO:
    def __init__(self, connection):
        self._connection = connection
        
        
    def create(self, username, password_hash):
        # Toteuta käyttäjän luominen tietokantaan
        cursor = self._connection.cursor()
        cursor.execute('''
            INSERT INTO users (username, password_hash) VALUES (?, ?)''',
            (username, password_hash)
        )
        self._connection.commit()
        
    def find_by_username(self, username):
        # Toteuta käyttäjään liittyvän haun toteutus
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        
        return row if row else None
