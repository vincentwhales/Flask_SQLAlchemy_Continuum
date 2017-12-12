from models import db
from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)

class Config(object):
  SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/continuum_testing'
  SQLALCHEMY_ECHO = True

app.config.from_object(Config)
db.init_app(app)

from user import User
migrate = Migrate(app, db)




