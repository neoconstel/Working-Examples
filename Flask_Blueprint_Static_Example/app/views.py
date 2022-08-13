from flask import Blueprint, render_template

views_bp = Blueprint("views", __name__, template_folder="templates", static_folder="static")


@views_bp.route("/")
def index():
    bp_root_path = views_bp.root_path
    return render_template("index.html", bp_root_path=bp_root_path)


@views_bp.route("/about")
def about():
    return "<h1>About Page</h1>"
