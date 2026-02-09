const API_BASE = '/api';

document.addEventListener('DOMContentLoaded', () => {
    loadTransactions();
    loadSummary();
    setTodayDate();

    document.getElementById('transaction-form').addEventListener('submit', handleAddTransaction);
});

function setTodayDate() {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('date').value = today;
}

async function handleAddTransaction(e) {
    e.preventDefault();

    const transaction = {
        type: document.getElementById('type').value,
        category: document.getElementById('category').value,
        amount: parseFloat(document.getElementById('amount').value),
        description: document.getElementById('description').value,
        date: document.getElementById('date').value
    };

    try {
        const response = await fetch(`${API_BASE}/transactions`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(transaction)
        });

        if (response.ok) {
            document.getElementById('transaction-form').reset();
            setTodayDate();
            loadTransactions();
            loadSummary();
        }
    } catch (error) {
        console.error('Error adding transaction:', error);
    }
}

async function loadTransactions() {
    try {
        const response = await fetch(`${API_BASE}/transactions`);
        const transactions = await response.json();

        const listDiv = document.getElementById('transactions-list');

        if (transactions.length === 0) {
            listDiv.innerHTML = '<p class="empty-message">No transactions yet. Add one to get started!</p>';
            return;
        }

        listDiv.innerHTML = transactions.map(t => `
            <div class="transaction-item">
                <div class="transaction-info">
                    <div class="transaction-category">${t.category}</div>
                    <div class="transaction-date">${new Date(t.date).toLocaleDateString()}</div>
                    ${t.description ? `<div class="transaction-description">${t.description}</div>` : ''}
                </div>
                <div class="transaction-amount ${t.type}">
                    ${t.type === 'income' ? '+' : '-'}$${parseFloat(t.amount).toFixed(2)}
                </div>
                <button class="btn-delete" onclick="deleteTransaction(${t.id})">Delete</button>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading transactions:', error);
    }
}

async function loadSummary() {
    try {
        const response = await fetch(`${API_BASE}/summary`);
        const summary = await response.json();

        document.getElementById('total-income').textContent = `$${summary.income.toFixed(2)}`;
        document.getElementById('total-expenses').textContent = `$${summary.expenses.toFixed(2)}`;
        document.getElementById('total-balance').textContent = `$${summary.balance.toFixed(2)}`;
    } catch (error) {
        console.error('Error loading summary:', error);
    }
}

async function deleteTransaction(id) {
    if (confirm('Are you sure you want to delete this transaction?')) {
        try {
            await fetch(`${API_BASE}/transactions/${id}`, { method: 'DELETE' });
            loadTransactions();
            loadSummary();
        } catch (error) {
            console.error('Error deleting transaction:', error);
        }
    }
}