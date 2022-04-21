from flask_restx import abort, Namespace, Resource, reqparse

from project.exceptions import ItemNotFound
from project.services import MoviesService
from project.setup_db import db
from project.tools.security import auth_required

movies_ns = Namespace("movies")
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)
parser.add_argument('status',type=str)


@movies_ns.route("/")
class MoviesView(Resource):
    @auth_required
    @movies_ns.expect(parser)
    @movies_ns.response(200, "OK")
    def get(self):
        """Get all movies"""
        req_args = parser.parser_args()
        if any (req_args.valuser()):
            return MoviesService(db.session).get_filter_movies(req_args)
        else:
            return MoviesService(db.session).get_all_movies()


@movies_ns.route("/<int:movie_id>")
class MovieView(Resource):
    @auth_required
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            return MoviesService(db.session).get_movie_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")