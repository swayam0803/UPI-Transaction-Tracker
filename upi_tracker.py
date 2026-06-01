import json
import os

# Filename to store transaction data locally
DATA_FILE = "transactions.json"

def load_transactions():
    """Loads transactions from a JSON file, or returns an empty list if none exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_transactions(transactions):
    """Saves the current transaction list to a local JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

def add_transaction(transactions):
    """Prompts user for input and appends a new transaction dictionary."""
    print("\n--- Add New UPI Transaction ---")
    try:
        amount = float(input("Enter Amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid number format. Transaction canceled.")
        return

    receiver = input("Enter Receiver Name / UPI ID: ").strip()
    category = input("Enter Category (e.g., Food, Shopping, Rent, Bills): ").strip().capitalize()
    
    # Create structured transaction object
    transaction = {
        "amount": amount,
        "receiver": receiver,
        "category": category
    }
    
    transactions.append(transaction)
    save_transactions(transactions)
    print(f"✅ Successfully logged ₹{amount} sent to {receiver}!")

def view_summary(transactions):
    """Performs analytical data processing on the transaction records."""
    print("\n--- Financial Analytics Summary ---")
    if not transactions:
        print("No transaction records found.")
        return

    total_spend = 0
    highest_expense = 0
    highest_receiver = "None"
    category_totals = {}
    anomaly_threshold = 10000  # Flags unusually large transactions
    anomalies = []

    for tx in transactions:
        amt = tx["amount"]
        cat = tx["category"]
        
        # Calculate totals
        total_spend += amt
        
        # Track the single highest transaction
        if amt > highest_expense:
            highest_expense = amt
            highest_receiver = tx["receiver"]
            
        # Aggregate spending by category
        category_totals[cat] = category_totals.get(cat, 0) + amt
        
        # Flag anomalies / unusual activity
        if amt >= anomaly_threshold:
            anomalies.append(tx)

    print(f"Total Transactions Logged: {len(transactions)}")
    print(f"Total Amount Spent: ₹{total_spend:,.2f}")
    print(f"Highest Single Expense: ₹{highest_expense:,.2f} (To: {highest_receiver})")
    
    print("\nSpending by Category:")
    for cat, total in category_totals.items():
        print(f" - {cat}: ₹{total:,.2f}")
        
    if anomalies:
        print(f"\n⚠️ Risk Alert: Detected {len(anomalies)} transaction(s) exceeding ₹{anomaly_threshold:,}!")
        for idx, tx in enumerate(anomalies, 1):
            print(f"   {idx}. ₹{tx['amount']:,} sent to {tx['receiver']} [{tx['category']}]")

def filter_by_category(transactions):
    """Filters data records using linear search scanning based on user criteria."""
    print("\n--- Filter Records by Category ---")
    if not transactions:
        print("No data available to filter.")
        return
        
    search_cat = input("Enter category to search for: ").strip().capitalize()
    print(f"\nShowing results for category: '{search_cat}'")
    print("-" * 45)
    
    count = 0
    for tx in transactions:
        if tx["category"] == search_cat:
            print(f"To: {tx['receiver']:<20} | Amount: ₹{tx['amount']:<10}")
            count += 1
            
    if count == 0:
        print("No matching records found for that category.")
    else:
        print(f"Found {count} records.")

def main():
    transactions = load_transactions()
    while True:
        print("\n==============================")
        print("   UPI TRANSACTION TRACKER   ")
        print("==============================")
        print("1. Add New Transaction")
        print("2. View Analytics Summary")
        print("3. Filter Transactions by Category")
        print("4. Exit Application")
        
        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_summary(transactions)
        elif choice == "3":
            filter_by_category(transactions)
        elif choice == "4":
            print("\nExiting program. Your financial data remains securely stored locally.")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
