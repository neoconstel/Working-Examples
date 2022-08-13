from flask_sqlalchemy import SQLAlchemy
from . import app
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	
