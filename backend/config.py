import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'portfolio-secret-key')
    DATABASE_PATH = os.environ.get('DATABASE_PATH', 'database.db')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'devpassword')

class TestConfig(Config):
    TESTING = True
    DATABASE_PATH = ':memory:'
