from flask_security import UserMixin, RoleMixin
from app import db

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avatar_url = db.Column(db.String)
    created = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    leaves = db.Column(db.Integer)
    level = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    mastery_level = db.Column(db.Integer)
    name = db.Column(db.String)
    personal_status_message = db.Column(db.String)
    total_achievements = db.Column(db.Integer)
    total_worshipers = db.Column(db.Integer)
    wins = db.Column(db.Integer)

    def __repr__(self):
        return '<Player {0}'.format(self.name)