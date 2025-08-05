# Define a class to represent a bank account
class BankAccount:
    
    # Constructor to initialize account details
    def __init__(self, name, account_number, balance=0):
        self.name = name                        # Account holder's name
        self.account_number = account_number    # Unique account number
        self.balance = balance                  # Initial balance (default is 0)
        print(f"Account created for {self.name} (A/C No: {self.account_number})")

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add amount to balance
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")  # Error for invalid deposit

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount  # Deduct amount from balance
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount.")  # Error for invalid withdrawal

    # Method to display current account details
    def display_balance(self):
        print("\n--- Account Details ---")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")
        print("------------------------")


# Example usage
# You can create an object of BankAccount like this:
# account = BankAccount("Abhishek", "1234567890", 1000)
# account.deposit(500)
# account.withdraw(200)
# account.display_balance()
