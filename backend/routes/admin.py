import os
from flask import Blueprint, request, jsonify, current_app
from config import Config
from models import list_contacts, get_contact

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/api/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json() or {}
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    expected_email = os.environ.get('ADMIN_EMAIL', Config.ADMIN_EMAIL)
    expected_password = os.environ.get('ADMIN_PASSWORD', Config.ADMIN_PASSWORD)

    if email != expected_email or password != expected_password:
        return jsonify({'success': False, 'error': 'Invalid login credentials.'}), 401

    return jsonify({'success': True, 'message': 'Login successful.'})

@admin_bp.route('/api/admin/messages', methods=['GET'])
def admin_messages():
    database_path = current_app.config.get('DATABASE_PATH', 'database.db')
    messages = list_contacts(database_path)
    return jsonify({'success': True, 'messages': messages})

@admin_bp.route('/api/admin/message/<int:message_id>', methods=['GET'])
def admin_message_detail(message_id):
    database_path = current_app.config.get('DATABASE_PATH', 'database.db')
    message = get_contact(database_path, message_id)
    if not message:
        return jsonify({'success': False, 'error': 'Message not found.'}), 404
    return jsonify({'success': True, 'message': message})
