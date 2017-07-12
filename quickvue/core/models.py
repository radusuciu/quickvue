"""Le models."""
from flask_security import UserMixin, RoleMixin
from marshmallow import Schema, fields, post_dump
from quickvue import db

Column = db.Column
Text = db.Text
Integer = db.Integer
relationship = db.relationship

roles_users = db.Table(
    'roles_users',
    Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    """Simple role or database user."""

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    description = Column(Text)


class User(db.Model, UserMixin):
    """User of proteomics database."""

    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=True)
    password = Column(Text)
    active = Column(Text)
    roles = relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic')
    )

class UserSchema(Schema):
    """Marshmallow schema for User."""

    id = fields.Integer(dump_only=True)
    email = fields.String()

    @post_dump(pass_many=True)
    def _wrap(self, data, many):
        return {'users': data} if many else data


user_schema = UserSchema()
