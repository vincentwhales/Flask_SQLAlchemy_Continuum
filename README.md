
Basic example demostrating combining SQLAlchemy with Flask-SQLAlchemy


1. Install requirements.txt via pip
2. Remove migrations/
3. Run `export FLASK_APP=app.py`
4. Run `flask db init`
5. Run `flask db migrate`
6. Look into migrations/version/X.py, there is no mention of _mod in there.
