from flask import Flask
from app.views import views_bp

app = Flask(__name__, static_folder=None)
app.register_blueprint(views_bp)


if __name__ == "__main__":
    app.run(debug=True)