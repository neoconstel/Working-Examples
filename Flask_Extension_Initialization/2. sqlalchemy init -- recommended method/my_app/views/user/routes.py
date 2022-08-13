from flask import current_app, Blueprint, render_template
user_bp = Blueprint('user_view', __name__, url_prefix='/user')

from my_app.models import db, User

@user_bp.route('/<name>')
def create_user(name):
	
	new_user = User()
	new_user.name = name
	db.session.add(new_user)
	db.session.commit()

	return f"New user, {name}, created and added to the database"
	
