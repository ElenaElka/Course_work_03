from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    favorite_genre = db.Column(db.Integer, db.ForeignKey("Genre.id"), nullable=False)
    genre = db.relationship("Genre")


    def __repr__(self):
        return f"<User'{self.name.title()}'>"