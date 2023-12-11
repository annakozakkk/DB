from typing import List
from datetime import datetime
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Server

class ServerDAO(GeneralDAO):
    _domain_type = Server

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(Server).filter(Server.name == name).all()

    def find_by_creation_date(self, creation_date: datetime) -> List[object]:
        return self._session.query(Server).filter(Server.creation_date == creation_date).all()
