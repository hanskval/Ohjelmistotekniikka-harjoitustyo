from src.UI.login_view import LoginView
from src.UI.create_user_view import CreateUserView
from src.UI.main_view import MainView
from src.UI.transaction_view import TransactionsView

class UI:
    def __init__(self, root, user_dao, transaction_dao,):
        self._root = root
        self._user_dao = user_dao
        self._transaction_dao = transaction_dao
        self._current_view = None  # Pitää kirjaa nykyisestä näkymästä
        self._transaction_dao = transaction_dao

    def start(self):
        # Näytetään ensimmäisenä ohjelman käynnityttyä
        self._show_login_view()

    def _hide_current_view(self):
        # Jos ruudulla on jo jokin näkymä, tuhotaan se ennen uuden näyttämistä
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        # Luodaan LoginView ja annetaan sille funktio, jota kutsua kun pitää vaihtaa näkymää
        self._current_view = LoginView(
            self._root,
            self._user_dao,
            self._show_create_user_view,
            self._show_main_view
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateUserView(
            self._root,
            self._user_dao,
            self._show_login_view
        )
        self._current_view.pack()
    
    def _show_main_view(self, user):
        self._hide_current_view()
        self._current_view = MainView(
            root=self._root,
            user_dao=self._user_dao,
            transaction_dao=self._transaction_dao,
            handle_logout=self._show_login_view,
            handle_show_transactions=self._show_transactions_view,
            user=user
        )
        self._current_view.pack()
        
    def _show_transactions_view(self, user):
        self._hide_current_view()
        self._current_view = TransactionsView(
            root=self._root,
            transaction_dao=self._transaction_dao,
            handle_back=lambda: self._show_main_view(user), # Takaisin päänäkymään
            user=user
        )
        self._current_view.pack()      
