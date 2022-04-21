import requests
from flask_restx import abort, Namespace, Resource, reqparse

from project.exceptions import ItemNotFound
from project.services import DirectorsService
from project.setup_db import db
from project.tools.security import auth_required

directors_ns = Namespace("directors")
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)


@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    @auth_required
    @directors_ns.expect(parser)
    def get(self):
        """Get all directors"""
        page = parser.parse_args().get("page")
        if page:
            return DirectorsService(db.session).get_limit_directors(page)
        else:
            return DirectorsService(db.session).get_all_directors()


@directors_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    @auth_required
    def get(self, director_id: int):
        """Get director by id"""
        try:
            return DirectorsService(db.session).get_director_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")