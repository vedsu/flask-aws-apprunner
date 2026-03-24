from flask import Blueprint, jsonify
from .model.webinar import get_all_webinars

# Define the blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/health')
def health():
    return jsonify({"status": "up", "service": "pharmaprofs-backend"}), 200

@main_bp.route('/webinar')
def webinar_list():
    data = get_all_webinars()
    return jsonify(data)
