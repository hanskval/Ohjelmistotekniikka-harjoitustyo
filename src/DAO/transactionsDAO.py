class TransactionsDAO:

    def __init__(self, connection):
        self._connection = connection

    def create(self, user_id, amount, category, description):
        cursor = self._connection.cursor()
        cursor.execute('''
            INSERT INTO transactions (user_id, amount, category, description)
            VALUES (?, ?, ?, ?)
        ''', (user_id, amount, category, description))
        self._connection.commit()

    def find_by_user_id(self, user_id):
        # Toteuta tapahtumien hakeminen käyttäjään liittyen
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT * FROM transactions WHERE user_id = ?
        ''', (user_id,))
        return cursor.fetchall()

    def get_balance(self, user_id):
        # Toteuta käyttäjään liittyvien tapahtumien summan laskeminen
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT SUM(amount) as balance FROM transactions WHERE user_id = ? ''', (user_id,))
        result = cursor.fetchone()
        return result['balance'] if result['balance'] is not None else 0.0

    def delete(self, transaction_id):
        # Toteuta tapahtuman poistaminen
        cursor = self._connection.cursor()
        cursor.execute('''
            DELETE FROM transactions WHERE id = ? ''', (transaction_id,))
        self._connection.commit()
