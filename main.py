# main.py

from bank_application import BankApplication

def main():
    # Create a bank application
    bank = BankApplication()

    # Create some accounts
    bank.create_account("1001", "Alice", 1000)
    bank.create_account("1002", "Bob", 500)

    # Queue some transactions
    bank.transaction_queue.enqueue({"account_number": "1001", "type": "deposit", "amount": 200})
    bank.transaction_queue.enqueue({"account_number": "1002", "type": "withdraw", "amount": 100})

    # Process the transactions
    bank.process_transactions()

    # Display all accounts
    print("All Accounts:")
    bank.display_all_accounts()

    # Get a statement for a specific account
    print("\nAccount Statement:")
    account = bank.find_account("1001")
    if account:
        account.get_statement()

if __name__ == "__main__":
    main()