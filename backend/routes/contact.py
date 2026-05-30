from flask import Blueprint, request, jsonify, current_app
from models import save_contact

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    if not name or not email or not subject or not message:
        return jsonify({'success': False, 'error': 'Please complete all fields.'}), 400

    database_path = current_app.config.get('DATABASE_PATH', 'database.db')
    contact_id = save_contact(database_path, name, email, subject, message)
    return jsonify({'success': True, 'message': 'Message submitted successfully.', 'contact_id': contact_id}), 201
