# Terminal-Based UPI Transaction Tracker

A lightweight, terminal-based Python application designed to log, store, and analyze personal financial transactions without relying on external dependencies.

## 🚀 Features
- **Transaction Logging:** Captures amount, receiver identity, and spending categories via terminal inputs.
- **Data Persistence:** Automatically reads and writes records to a local `transactions.json` file.
- **Financial Analytics Engine:** Computes real-time data metrics including total spending, top expenses, and category-wise breakdowns.
- **Anomaly Detection:** Scans transactions using conditional loops to flag any unusual transactions exceeding ₹10,000.
- **Linear Search Filter:** Allows users to parse and filter transaction histories instantly by specific categories.

## 🛠️ Technologies Used
- **Language:** Python 3
- **Built-in Modules:** `json`, `os`

## ⚙️ How To Run
1. Clone this repository or download `upi_tracker.py`.
2. Open your terminal and run:
   ```bash
   python upi_tracker.py
   ```
