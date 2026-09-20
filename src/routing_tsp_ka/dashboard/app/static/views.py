import os

from flask import Blueprint, current_app, render_template
from flask_cors import CORS

bp = Blueprint('main', __name__)
CORS(bp, resources={r"/receive": {"origins": "*"}})

IMAGE_FOLDER = 'src/routing_tsp_ka/dashboard/app/static/images'  # Define a subfolder within static
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@bp.route('/')
def index() -> str:
    """Main page of the dashboard.

    Routes the Flask application to the main page.
    """
    return render_template('index.html',
                          cadenza_uri=current_app.config.get('CADENZA_URI'),
                          config=current_app.config)

@bp.route('/receive', methods=['post'])
def receive():
    """Placeholder for receiving POST requests.

    Needs to be updated later on.
    """
    print("Received POST request at /receive")