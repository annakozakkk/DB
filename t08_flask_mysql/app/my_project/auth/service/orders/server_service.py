from t08_flask_mysql.app.my_project.auth.dao import server_dao
from t08_flask_mysql.app.my_project.auth.dao.orders import channel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ServerService(GeneralService):
    """
    Realisation of Server service.
    """
    _dao = server_dao
