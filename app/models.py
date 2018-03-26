from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    fullname = db.Column(db.String(120), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    entries = db.relationship('Entry', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Full Name {} [Nick: {}, Email {}]'.format(self.fullname, self.username, self.email)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(40), index = True)
    body = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Entry {}>'.format(self.body)

