# bank_application.py

from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount):
        self.date = datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount

    def __str__(self):
        return f"{self.date}: {self.transaction_type} ${self.amount:.2f}"

class LinkedList:
    class Node:
        def __init__(self, transaction):
            self.transaction = transaction
            self.next = None

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, transaction):
        new_node = self.Node(transaction)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.transaction)
            current = current.next

class Account:
    def __init__(self, account_number, customer_name, initial_balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transaction_history = LinkedList()

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.insert_at_beginning(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.insert_at_beginning(Transaction("Withdrawal", amount))
            return True
        return False

    def get_statement(self):
        print(f"Account Statement for {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("Transaction History:")
        self.transaction_history.display()

class BSTNode:
    def __init__(self, account):
        self.account = account
        self.left = None
        self.right = None

    def insert(self, account):
        if account.account_number < self.account.account_number:
            if self.left:
                self.left.insert(account)
            else:
                self.left = BSTNode(account)
        else:
            if self.right:
                self.right.insert(account)
            else:
                self.right = BSTNode(account)

    def search(self, account_number):
        if self.account.account_number == account_number:
            return self.account
        if account_number < self.account.account_number and self.left:
            return self.left.search(account_number)
        if account_number > self.account.account_number and self.right:
            return self.right.search(account_number)
        return None

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(f"Account: {self.account.account_number}, Balance: ${self.account.balance:.2f}")
        if self.right:
            self.right.in_order_traversal()

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return

class BankApplication:
    def __init__(self):
        self.accounts_bst = None
        self.transaction_queue = Queue()
        self.customer_hash = HashTable()

    def create_account(self, account_number, customer_name, initial_balance):
        new_account = Account(account_number, customer_name, initial_balance)
        if not self.accounts_bst:
            self.accounts_bst = BSTNode(new_account)
        else:
            self.accounts_bst.insert(new_account)
        self.customer_hash.insert(customer_name, new_account)

    def find_account(self, account_number):
        if self.accounts_bst:
            return self.accounts_bst.search(account_number)
        return None

    def find_customer(self, customer_name):
        return self.customer_hash.search(customer_name)

    def process_transactions(self):
        while not self.transaction_queue.is_empty():
            transaction = self.transaction_queue.dequeue()
            account = self.find_account(transaction['account_number'])
            if account:
                if transaction['type'] == 'deposit':
                    account.deposit(transaction['amount'])
                elif transaction['type'] == 'withdraw':
                    account.withdraw(transaction['amount'])

    def display_all_accounts(self):
        if self.accounts_bst:
            self.accounts_bst.in_order_traversal()

    def get_all_accounts(self):
        accounts = []
        def inorder(node):
            if node:
                inorder(node.left)
                accounts.append(node.account)
                inorder(node.right)
        inorder(self.accounts_bst)
        return accounts