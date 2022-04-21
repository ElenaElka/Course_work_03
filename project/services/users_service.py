from project.dao import UserDAO
from project.dao.models import User
from project.exceptions import ItemNotFound
from project.schemas.user import UserSchema
from project.services.base import BaseService


class UsersService(BaseService):
    def get_user_by_name(self, name):
        user = UserDAO(self._db_session).get_user_by_name(name)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)


    def get_user_by_email(self, email):
        user = UserDAO(self._db_session).get_user_by_email(email)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)


    def create(self, new_user):
        obj = User(**new_user)
        self._db_session.add(obj)
        self._db_session.commit()
        return obj


    def patch(self, data):
        uid = data.get("id")
        user = self.get_user_by_name(uid)

        if "name" in data:
           user.name = data.get("name")
        if "surname" in data:
           user.surname = data.get("surname")
        if "favorite_genre" in data:
           user.surname = data.get("favorite_genre")
        return UserSchema().dump(user)


    def put(self, users_data):
        uid = users_data.get("id")
        user = self.get_user_by_name(uid)

        if "password_1" in users_data:
           user.password_1 = users_data.get("password_1")
        if "password_2" in users_data:
           user.password_2 = users_data.get("password_2")
        return UserSchema().dump(user)