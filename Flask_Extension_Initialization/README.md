# Flask extension initialization using the factory app design pattern

Flask extensions (e.g flask_sqlalchemy, flask_mail etcetera) can be immediately initialized with the flask app upon creation. Using flask_sqlalchemy as an example, in such a case would have:
	> db = SQLAlchemy(app)

However, for standard reasons, it is desired to have the database initialized on its own without any app tied to it. This is to ensure that the database object, db, stands alone and can be used by any flask app if there are more than one in our program (flask app here referes to the object created when we say app = Flask(__name__) ). Initializing a flask extension independently and later initializing it with the app when needed would look like this:
	> db = SQLAlchemy()		(this could be in an extensions.py script dedicated only for defining extensions)
	> db.init_app(app=app)		(this is usually in the initializations script, after importing from where db was originally defined)
	

In this example guide, two examples are shown: the WRONG way of initializing flask extensions, as well as the RECOMMENDED method (using the factory app design pattern). Both examples work, as well as use flask blueprints. The original documentation where this concept can be read about in detail can be found here: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/


