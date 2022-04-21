from flask import current_app

from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genre import GenreSchema
from project.services.base import BaseService


class GenresService(BaseService):
    def get_item_by_id(self, pk):
        genre = GenreDAO(self._db_session).get_by_id(pk)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all_genres(self):
        genres = GenreDAO(self._db_session).get_all()
        return GenreSchema(many=True).dump(genres)

    def get_genrs_genres(self, page):
        limit = current_app.config["ITEMS_PER_PAGE"]
        offset = (page - 1) + limit
        genres = GenreDAO(self._db_session).get_genre_limit(limit=limit, offset=offset)
        return GenreSchema(many=True).dump(genres)