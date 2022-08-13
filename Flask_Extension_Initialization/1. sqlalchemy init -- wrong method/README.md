## Why this method is not recommended, even though it works:

- the database object (db) is tied to the app because it was created directly by initializing it with the app: < db = SQLAlchemy(app) >.
	The reason why this is not wanted is due to reasons of flexibility in using the database for other apps.
	
	> We can work around this by using the factory design pattern to first create the app from a function and then initialize
	the database with the createed app, as explained here: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
	
- the database is also tied to the particular model script

	> We can solve this by creating the database object in a separate extensions.py script, dedicated for all extensions such
	as flask_sqlalchemy, flask_mail etc.
