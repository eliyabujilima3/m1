import sqlite3
from datetime import datetime

CREATE_CONTACT_TABLE = '''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TEXT NOT NULL,
    replied INTEGER NOT NULL DEFAULT 0
);
'''

CREATE_REPLIES_TABLE = '''
CREATE TABLE IF NOT EXISTS replies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_id INTEGER NOT NULL,
    response TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(contact_id) REFERENCES contacts(id)
);
'''


def get_connection(database_path):
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(database_path):
    connection = get_connection(database_path)
    cursor = connection.cursor()
    cursor.execute(CREATE_CONTACT_TABLE)
    cursor.execute(CREATE_REPLIES_TABLE)
    connection.commit()
    connection.close()


def save_contact(database_path, name, email, subject, message):
    connection = get_connection(database_path)
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO contacts (name, email, subject, message, created_at) VALUES (?, ?, ?, ?, ?)',
        (name, email, subject, message, datetime.utcnow().isoformat())
    )
    connection.commit()
    contact_id = cursor.lastrowid
    connection.close()
    return contact_id


def list_contacts(database_path):
    connection = get_connection(database_path)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
    rows = cursor.fetchall()
    connection.close()
    return [dict(row) for row in rows]


def get_contact(database_path, contact_id):
    connection = get_connection(database_path)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
    row = cursor.fetchone()
    connection.close()
    return dict(row) if row else None


def mark_replied(database_path, contact_id):
    connection = get_connection(database_path)
    cursor = connection.cursor()
    cursor.execute('UPDATE contacts SET replied = 1 WHERE id = ?', (contact_id,))
    connection.commit()
    connection.close()


def save_reply(database_path, contact_id, response):
    connection = get_connection(database_path)
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO replies (contact_id, response, created_at) VALUES (?, ?, ?)',
        (contact_id, response, datetime.utcnow().isoformat())
    )
    connection.commit()
    connection.close()
import sqlite3
from datetime import datetime

CREATE_CONTACTS = '''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TEXT NOT NULL
);
'''

CREATE_REPLIES = '''
CREATE TABLE IF NOT EXISTS replies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_id INTEGER NOT NULL,
    reply TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(contact_id) REFERENCES contacts(id)
);
'''


def get_connection(db_path):
    connection = sqlite3.connect(db_path, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(db_path):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(CREATE_CONTACTS)
    cursor.execute(CREATE_REPLIES)
    conn.commit()
    conn.close()


def save_contact(db_path, name, email, subject, message):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO contacts (name, email, subject, message, created_at) VALUES (?, ?, ?, ?, ?)',
        (name, email, subject, message, datetime.utcnow().isoformat())
    )
    conn.commit()
    contact_id = cursor.lastrowid
    conn.close()
    return contact_id


def get_messages(db_path):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_message(db_path, message_id):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts WHERE id = ?', (message_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def save_reply(db_path, contact_id, reply_text):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO replies (contact_id, reply, created_at) VALUES (?, ?, ?)',
        (contact_id, reply_text, datetime.utcnow().isoformat())
    )
    conn.commit()
    reply_id = cursor.lastrowid
    conn.close()
    return reply_id


def get_replies(db_path, contact_id=None):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    if contact_id:
        cursor.execute('SELECT * FROM replies WHERE contact_id = ? ORDER BY created_at DESC', (contact_id,))
    else:
        cursor.execute('SELECT * FROM replies ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
