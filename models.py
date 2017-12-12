from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from sqlalchemy_continuum import make_versioned, versioning_manager
from sqlalchemy_continuum.plugins import FlaskPlugin, PropertyModTrackerPlugin

make_versioned(plugins=[FlaskPlugin()])
versioning_manager.plugins.append(PropertyModTrackerPlugin())

print versioning_manager.plugins


