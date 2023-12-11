from datetime import datetime
from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Game


class GameDAO(GeneralDAO):
    _domain_type = Game

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(Game).filter(Game.name == name).order_by(Game.name).all()

    def find_by_release_date(self, release_date: datetime) -> List[object]:
        return self._session.query(Game).filter(Game.release_date == release_date).order_by(Game.release_date).all()
