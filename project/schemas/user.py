from marshmallow import fields, Schema


class UserSchema(Schema):
    email = fields.Int(required=True)
    password = fields.Int(required=True)
    name = fields.Int(required=True)
    surname = fields.Int(required=True)
    favorite_genre  = fields.Int(required=True)