from marshmallow import fields, Schema


class MovieSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    trailer = fields.Str(required=True)
    year = fields.Str(required=True)
    rating  = fields.Str(required=True)
    genre_id = fields.Str(required=True)
    genre = fields.Str(required=True)
    director_id = fields.Str(required=True)
    director = fields.Str(required=True)