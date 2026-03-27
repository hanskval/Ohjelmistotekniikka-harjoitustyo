from src.UI.login_view import LoginView
from src.UI.create_user_view import CreateUserView
class UI:
    def __init__(self, root, user_dao):
        self._root = root
        self._user_dao = user_dao
        self._current_view = None # Pitää kirjaa nykyisestä näkymästä

    def start(self):
        # Kun ohjelma käynnistyy, näytetään ensimmäisenä kirjautuminen
        self._show_login_view()

    def _hide_current_view(self):
        # Jos ruudulla on jo jokin näkymä, tuhotaan sen kaikki elementit
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        # Luodaan LoginView ja annetaan sille funktio, jota kutsua kun pitää vaihtaa näkymää
        self._current_view = LoginView(
            self._root,
            self._user_dao,
            self._show_create_user_view # Annetaan funktio argumenttina!
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()
        # Luodaan CreateUserView ja annetaan sille paluufunktio
        self._current_view = CreateUserView(
            self._root,
            self._user_dao,
            self._show_login_view
        )
        self._current_view.pack()