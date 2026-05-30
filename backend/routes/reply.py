from flask import Blueprint, request, jsonify, current_app
from models import save_reply, mark_replied

reply_bp = Blueprint('reply', __name__)

@reply_bp.route('/api/reply', methods=['POST'])
def send_reply():
    data = request.get_json() or {}
    contact_id = data.get('contact_id')
    response_text = data.get('reply', '').strip()

    if not contact_id or not response_text:
        return jsonify({'success': False, 'error': 'Contact ID and reply text are required.'}), 400

    database_path = current_app.config.get('DATABASE_PATH', 'database.db')
    save_reply(database_path, contact_id, response_text)
    mark_replied(database_path, contact_id)

    return jsonify({'success': True, 'message': 'Reply saved successfully.'})
