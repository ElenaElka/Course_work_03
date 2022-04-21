import requests
from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services import UsersService
from project.setup_db import db
from project.tools.security import auth_required

users_ns = Namespace("users")


@users_ns.route("/<str:user_name>")
class UserView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "User not found")
    def get(self, user_name: str):
        """Get genre by name"""
        try:
            return UsersService(db.session).get_user_by_name(user_name)
        except ItemNotFound:
            abort(404, message="User not found")


    def patch(self, user_name: str):
        req_json = requests.json
        if not req_json:
            abort(400, massage="Bad Request")
        if not req_json.get('name'):
            req_json["name"] = user_name
        try:
            return UsersService(db.session).update(req_json)
        except ItemNotFound:
            abort(404, message="User not found")


@users_ns.route("/password/<int: user_id>")
class UserView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "User not found")
    def put(self, user_id:int):
        req_json = requests.json
        if not req_json:
            abort(400, massage="Bad Request")
        if not req_json.get('password_1') or not req_json.get('password_2'):
            abort(400, massage="Bad Request")
        if not req_json.get('id'):
            req_json['id'] = user_id
        try:
            return UsersService(db.session).update_pass(req_json)
        except ItemNotFound:
            abort(404, message="User not found")