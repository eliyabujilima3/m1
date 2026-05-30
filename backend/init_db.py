from config import Config
from models import init_db

if __name__ == '__main__':
    config = Config()
    init_db(config.DATABASE_PATH)
    print(f"Database initialized at {config.DATABASE_PATH}")
