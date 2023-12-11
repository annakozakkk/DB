from t08_flask_mysql.app.my_project.auth.dao import message_dao
from t08_flask_mysql.app.my_project.auth.dao.orders import channel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class MessageService(GeneralService):
    """
    Realisation of Message service.
    """
    _dao = message_dao
