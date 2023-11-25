from datetime import datetime
from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Message


class MessageDAO(GeneralDAO):
    _domain_type = Message

    def find_by_user_id(self, user_id: int) -> List[object]:
        return self._session.query(Message).filter(Message.user_id == user_id).order_by(Message.user_id).all()

    def find_by_message_text(self, message_text: str) -> List[object]:
        return self._session.query(Message).filter(Message.message_text == message_text).order_by(
            Message.message_text).all()

    def find_by_timestamp(self, timestamp: datetime) -> List[object]:
        return self._session.query(Message).filter(Message.timestamp == timestamp).order_by(Message.timestamp).all()
