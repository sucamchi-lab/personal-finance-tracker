from flask import Flask, render_template, request, jsonify
from database import init_db
from models import Transaction
from datetime import datetime

app = Flask(__name__)

# Initialize database on startup


@app.before_request
def startup():
    init_db()

# Routes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.get_all_transactions()
    return jsonify(transactions)


@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    try:
        transaction_id = Transaction.add_transaction(
            type=data['type'],
            category=data['category'],
            amount=float(data['amount']),
            description=data.get('description', ''),
            date=data['date']
        )
        return jsonify({'success': True, 'id': transaction_id}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    try:
        Transaction.delete_transaction(id)
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/summary', methods=['GET'])
def get_summary():
    summary = Transaction.get_summary()
    return jsonify(summary)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
