from flask import Flask, redirect, url_for
from .models import db
import os

def create_app():
	app = Flask(__name__)
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
	app.config["dev"] = "neoconstel" # just experimenting using current_app in a blueprint view (check the admin view) to access the app context
	
	#register blueeprints
	from .views.admin.routes import admin_bp
	from .views.user.routes import user_bp
	app.register_blueprint(admin_bp)
	app.register_blueprint(user_bp)
	
	
	@app.route("/")
	def root():
		return redirect(url_for('admin_view.admin'))
		
		
	db.init_app(app)
	
	# to be sure we won't overwrite an existing database
	if not os.path.exists("my_app/data.db"):
		print("\nNo database. Creating one now\n")
		db.create_all(app=app)
	else:
		print("\nDatabase found\n")
	
	return app
	
	

