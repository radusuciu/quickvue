"""Le models."""
from flask_security import UserMixin, RoleMixin
from marshmallow import Schema, fields, post_dump
from quickvue import db, db_wrapper
from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    TextField
)

class BaseModel(db_wrapper.Model):
    class Meta:
        database = db

class Role(BaseModel, RoleMixin):
    """Simple role or database user."""
    name = CharField(unique=True)
    description = TextField(null=True)

class User(BaseModel, UserMixin):
    email = TextField(unique=True)
    password = TextField()
    active = BooleanField(default=True)

class UserRoles(BaseModel):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)

class UserSchema(Schema):
    """Marshmallow schema for User."""

    id = fields.Integer(dump_only=True)
    email = fields.String()

    @post_dump(pass_many=True)
    def _wrap(self, data, many):
        return {'users': data} if many else data


user_schema = UserSchema()
