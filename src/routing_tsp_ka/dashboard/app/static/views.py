from flask import Blueprint, render_template, request, jsonify, current_app
import os
from flask_cors import CORS


bp = Blueprint('main', __name__)
CORS(bp, resources={r"/receive": {"origins": "*"}})

IMAGE_FOLDER = 'src/routing_tsp_ka/dashboard/app/static/images'  # Define a subfolder within static
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@bp.route('/')
def index():
    return render_template('index.html',
                          cadenza_uri=current_app.config.get('CADENZA_URI'),
                          config=current_app.config)

@bp.route('/receive', methods=['post'])
def receive():
    print("Received POST request at /receive")