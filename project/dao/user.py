from sqlalchemy.orm.scoping import scoped_session

from project.dao.models import User



class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_user_by_name(self, user_name):
        return self._db_session.query(User).filter(User.name == user_name).one_or_none()

    def get_user_by_email(self, user_email):
        return self._db_session.query(User).filter(User.email == user_email).one_or_none()

    def put_user(self, user):
        self._db_session.add(user)
        self._db_session.commit()
        return user