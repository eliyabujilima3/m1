import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from routes.contact import contact_bp
from routes.admin import admin_bp
from routes.reply import reply_bp
from models import init_db


def create_app(testing=False):
    app = Flask(__name__)

    # Load env first
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

    # Load config
    app.config.from_object(Config())

    if testing:
        from config import TestConfig
        app.config.from_object(TestConfig())

    # Enable CORS
    CORS(app)

    # Register blueprints
    app.register_blueprint(contact_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(reply_bp)

    # ✅ FIX: replace before_first_request
    def prepare_database():
        database_path = app.config.get('DATABASE_PATH')
        if database_path:
            init_db(database_path)

    # Run once during app startup (Flask 3 safe way)
    with app.app_context():
        prepare_database()

    @app.route('/api/status')
    def status():
        return jsonify({
            'status': 'ok',
            'message': 'Portfolio API is running'
        })

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)