from flask import Blueprint, render_template

admin_app = Blueprint('admin', __name__)

@admin_app.route('/')
def home():
    return render_template('/admin/admin.html')