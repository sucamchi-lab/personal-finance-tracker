<div align="center">

# 💸 Personal Finance Tracker

### _Track every dollar. Understand your habits. Build better money routines._

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

<img src="https://img.icons8.com/3d-fluency/256/money-bag-euro.png" width="110" alt="Finance icon" />

<br/>

**A simple, intuitive personal finance app built with Flask + SQLite to log transactions, monitor your balance, and stay financially organized.**

[Motivation](#-motivation) · [Features](#-features) · [Quick Start](#-quick-start) · [Usage](#-usage) · [Contributing](#-contributing)

</div>

---

## 💡 Motivation

Managing personal money should not feel complicated.

Many people track expenses inconsistently, forget where money went, and only review finances when something feels wrong.

**Personal Finance Tracker** keeps things simple: add income and expenses, categorize transactions, and instantly see where you stand.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 💰 Income & Expense Tracking

- Add transactions in seconds
- Clearly label each entry as income or expense
- Keep your records centralized in one place

</td>
<td width="50%">

### 📊 Instant Financial Summary

- View total income, total expenses, and balance
- Understand your current financial status at a glance
- Monitor changes as you add new transactions

</td>
</tr>
<tr>
<td width="50%">

### 🏷️ Categories & Organization

- Assign categories to each transaction
- Improve visibility into spending patterns
- Make your history easier to review

</td>
<td width="50%">

### 📅 Date Filtering

- Filter transactions by date
- Focus on specific periods (daily/weekly/monthly)
- Speed up budget check-ins

</td>
</tr>
<tr>
<td width="50%">

### 🗑️ Easy Cleanup

- Delete incorrect or outdated transactions
- Keep your financial log accurate

</td>
<td width="50%">

### 📱 Responsive Interface

- Works on desktop and mobile screens
- Clean layout with no extra complexity

</td>
</tr>
</table>

---

## ⚡ Quick Start

### Prerequisites

- Python 3.x
- `pip`

### Installation & Run

```bash
# Clone the repository
git clone https://github.com/sucamchi-lab/personal-finance-tracker.git

# Enter the project
cd personal-finance-tracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the app
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

To deactivate the environment later:

```bash
deactivate
```

---

## 📖 Usage

Getting started is simple:

```
1️⃣  Add transaction  →  Record income/expense with category and date
2️⃣  Review summary   →  Check totals and current balance
3️⃣  Filter & refine  →  Filter by date and remove unwanted entries
```

### Example flow

| Action                  | Result                              |
| ----------------------- | ----------------------------------- |
| Add salary transaction  | Increases total income              |
| Add grocery expense     | Increases total expenses            |
| Open dashboard summary  | Shows updated net balance           |
| Filter by current month | Focuses analysis on recent activity |

---

## 🛠️ Built With

- **Flask** — backend routes and server logic
- **SQLite** — lightweight local database
- **HTML/CSS/JavaScript** — frontend interface

---

## 📂 Project Structure

```text
personal-finance-tracker/
├── app.py
├── database.py
├── models.py
├── requirements.txt
├── static/
│   ├── script.js
│   └── style.css
└── templates/
    └── index.html
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

<div align="center">

## 🌟 Keep your money visible, and your decisions intentional.

If this project helped you, consider leaving a ⭐ on the repo.

</div>
