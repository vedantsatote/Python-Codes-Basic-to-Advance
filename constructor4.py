class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

# Creating an instance of BankAccount
account1 = BankAccount("John Doe", 500.0)

# Performing operations
account1.deposit(200)
account1.withdraw(100)
account1.display_balance()

# Creating another instance with default balance
account2 = BankAccount("Jane Smith")
account2.display_balance()
