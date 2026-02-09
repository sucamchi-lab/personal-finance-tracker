import sqlite3
from datetime import datetime


def init_db():
    """Initialize the database with tables"""
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    # Create transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create categories table (optional, for predefined categories)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            type TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def get_db_connection():
    """Get a database connection"""
    conn = sqlite3.connect('finance.db')
    conn.row_factory = sqlite3.Row
    return conn
