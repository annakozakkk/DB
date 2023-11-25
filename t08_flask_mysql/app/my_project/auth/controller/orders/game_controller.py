
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import game_service


class GameController(GeneralController):
    """
    Realisation of Game controller.
    """
    _service = game_service
