from models import db

class User(db.Model):
    __tablename__ = 'users'
    __versioned__ = {}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(255))
    age = db.Column(db.Integer)


