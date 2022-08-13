from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["dev"] = "neoconstel"

from .models import db

db.create_all()


@app.route("/")
def home():
	return f"HOME -- developed by {app.config.get('dev')}"
	

