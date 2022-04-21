from flask import request
from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound
from project.services.users_service import UsersService
from project.setup_db import db
from project.tools.security import login_user, refresh_user_token

auth_ns = Namespace('auth')


@auth_ns.route('/login')
class AuthView(Resource):
    """Add new user"""
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad Request")
        try:
            user = UsersService(db.session).get_user_by_email(email=req_json.get("email"))
            tokens = login_user(request.json, user)
            return tokens, 200
        except ItemNotFound:
            abort(401, message="Authorization Error")

    """Update password"""
    def put(self):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad Request")
        try:
            tokens = refresh_user_token(req_json)
            return tokens, 200
        except ItemNotFound:
            abort(401, message="Authorization Error")


"""New user registration"""
@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad Request")
        return UsersService(db.session).create(req_json)