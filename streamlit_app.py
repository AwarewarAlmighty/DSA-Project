# streamlit_app.py

import streamlit as st
from bank_application import BankApplication

# Initialize session state
if 'bank' not in st.session_state:
    st.session_state.bank = BankApplication()

def main():
    st.title("Simple Bank Application")

    # Sidebar for adding new accounts
    with st.sidebar:
        st.header("Create New Account")
        account_number = st.text_input("Account Number")
        customer_name = st.text_input("Customer Name")
        initial_balance = st.number_input("Initial Balance", min_value=0.0, value=0.0, step=10.0)
        if st.button("Create Account"):
            st.session_state.bank.create_account(account_number, customer_name, initial_balance)
            st.success(f"Account {account_number} created successfully!")

    # Main area for displaying accounts and transactions
    st.header("Accounts Overview")
    accounts = st.session_state.bank.get_all_accounts()
    for account in accounts:
        st.subheader(f"Account: {account.account_number}")
        st.write(f"Customer: {account.customer_name}")
        st.write(f"Balance: ${account.balance:.2f}")

        # Transaction options
        transaction_type = st.selectbox(f"Transaction for {account.account_number}", ["Deposit", "Withdraw"], key=account.account_number)
        amount = st.number_input("Amount", min_value=0.0, step=10.0, key=f"amount_{account.account_number}")
        if st.button("Perform Transaction", key=f"transaction_{account.account_number}"):
            if transaction_type == "Deposit":
                account.deposit(amount)
                st.success(f"Deposited ${amount:.2f} to account {account.account_number}")
            else:
                if account.withdraw(amount):
                    st.success(f"Withdrew ${amount:.2f} from account {account.account_number}")
                else:
                    st.error("Insufficient funds!")

        # Display transaction history
        if st.button("Show Transaction History", key=f"history_{account.account_number}"):
            st.write("Transaction History:")
            current = account.transaction_history.head
            while current:
                st.write(current.transaction)
                current = current.next

        st.markdown("---")

if __name__ == "__main__":
    main()