from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db

class Role(db.Model):
    __tablename__ = 'role'
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(200))

    # users = db.relationship("User", secondary="user_role_association", back_populates="roles")

    def __repr__(self) -> str:
        return f"Role({self.role_id}, {self.name}, {self.description})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "role_id": self.role_id,
            "name": self.name,
            "description": self.description,
            # "users": [user.put_into_dto() for user in self.users],


        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Role:
        obj = Role(
            role_id=dto_dict.get("role_id"),
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
        )
        return obj




