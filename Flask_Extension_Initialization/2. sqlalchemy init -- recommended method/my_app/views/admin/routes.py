from flask import current_app, Blueprint, render_template
admin_bp = Blueprint('admin_view', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin():
    return f"ADMIN -- made by {current_app.config.get('dev')}"
