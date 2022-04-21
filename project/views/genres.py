from flask_restx import abort, Namespace, Resource, reqparse

from project.exceptions import ItemNotFound
from project.services import GenresService
from project.setup_db import db
from project.tools.security import auth_required
from project.views.directors import parser

genres_ns = Namespace("genres")
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)


@genres_ns.route("/")
class GenresView(Resource):
    @auth_required
    @genres_ns.expect(parser)
    @genres_ns.response(200, "OK")
    def get(self):
        """Get all genres"""
        page = parser.parse_args().get("page")
        if page:
            return GenresService(db.session).get_genre_limit(page)
        else:
            return GenresService(db.session).get_all_genres()


@genres_ns.route("/<int:genre_id>")
class GenreView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def get(self, genre_id: int):
        """Get genre by id"""
        try:
            return GenresService(db.session).get_item_by_id(genre_id)
        except ItemNotFound:
            abort(404, message="Genre not found")