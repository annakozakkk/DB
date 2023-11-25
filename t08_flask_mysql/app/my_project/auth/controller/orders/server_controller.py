
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import  server_service


class ServerController(GeneralController):
    """
    Realisation of Server controller.
    """
    _service = server_service
