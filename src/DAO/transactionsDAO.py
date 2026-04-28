class TransactionsDAO:
    """ Toteuttaa tapahtumiin liittyviä tietokantaoperaatioita """

    def __init__(self, connection):
        self._connection = connection

    def create(self, user_id, amount, category, description):
        """ Toteuttaa tapahtuman luomisen tietokantaan """
        cursor = self._connection.cursor()
        cursor.execute('''
            INSERT INTO transactions (user_id, amount, category, description)
            VALUES (?, ?, ?, ?)
        ''', (user_id, amount, category, description))
        self._connection.commit()

    def find_by_user_id(self, user_id):
        """ Toteutta tapahtumien hakemisen käyttäjään liittyen tietokannasta """
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT * FROM transactions WHERE user_id = ?
        ''', (user_id,))
        return cursor.fetchall()

    def get_income(self, user_id):
        """ Toteutta tulojen haku käyttäjään liittyen tietokannasta """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT SUM(amount) FROM transactions WHERE user_id = ? AND amount > 0", 
            (user_id,)
        )
        result = cursor.fetchone()[0]

        return result if result is not None else 0.0

    def get_expenses(self, user_id):
        """ Toteutta kustannusten haku käyttäjään liittyen tietokannasta """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT SUM(amount) FROM transactions WHERE user_id = ? AND amount < 0", 
            (user_id,)
        )
        result = cursor.fetchone()[0]

        return result if result is not None else 0.0

    def get_balance(self, user_id):
        """ Toteutta käyttäjään liittyvien tapahtumien summan laskeminen """
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT SUM(amount) as balance FROM transactions WHERE user_id = ? ''', (user_id,))
        result = cursor.fetchone()
        return result['balance'] if result['balance'] is not None else 0.0

    def delete(self, transaction_id):
        """ Toteuttaa tapahtuman poistamisen tietokannasta """
        cursor = self._connection.cursor()
        cursor.execute('''
            DELETE FROM transactions WHERE id = ? ''', (transaction_id,))
        self._connection.commit()
