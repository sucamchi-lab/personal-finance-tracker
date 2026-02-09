from database import get_db_connection
from datetime import datetime


class Transaction:
    @staticmethod
    def add_transaction(type, category, amount, description, date):
        """Add a new transaction"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (type, category, amount, description, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (type, category, amount, description, date))
        conn.commit()
        conn.close()
        return cursor.lastrowid

    @staticmethod
    def get_all_transactions():
        """Get all transactions"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
        transactions = cursor.fetchall()
        conn.close()
        return [dict(t) for t in transactions]

    @staticmethod
    def get_transactions_by_category(category):
        """Get transactions filtered by category"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM transactions WHERE category = ? ORDER BY date DESC', (category,))
        transactions = cursor.fetchall()
        conn.close()
        return [dict(t) for t in transactions]

    @staticmethod
    def delete_transaction(id):
        """Delete a transaction"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM transactions WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_summary():
        """Get income and expense summary"""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            'SELECT SUM(amount) as total FROM transactions WHERE type = "income"')
        income = cursor.fetchone()['total'] or 0

        cursor.execute(
            'SELECT SUM(amount) as total FROM transactions WHERE type = "expense"')
        expenses = cursor.fetchone()['total'] or 0

        conn.close()
        return {'income': income, 'expenses': expenses, 'balance': income - expenses}
