from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(150))
    totalN5 = db.Column(db.Integer)
    totalN4 = db.Column(db.Integer)
    totalN3 = db.Column(db.Integer)
    totalN2 = db.Column(db.Integer)
    totalN1 = db.Column(db.Integer)
    knownN5 = db.Column(db.Integer)
    knownN4 = db.Column(db.Integer)
    knownN3 = db.Column(db.Integer)
    knownN2 = db.Column(db.Integer)
    knownN1 = db.Column(db.Integer)
    unknownKanji = db.Column(db.String(2200))
    readPercentage = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    knownKnaji = db.Column(db.String(2200))
    url = db.relationship("Url")