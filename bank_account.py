# bank_account.py
# A simple Bank Account simulation using OOP concepts

class BankAccount:
    """
    Base class for a bank account
    Demonstrates encapsulation and core banking operations
    """

    def __init__(self, account_number, holder_name, balance=0):
        # Protected attributes (encapsulation)
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = balance

    # Getter methods (encapsulation)
    def get_account_number(self):
        return self._account_number

    def get_holder_name(self):
        return self._holder_name

    def get_balance(self):
        return self._balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Display account details
    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self._account_number}")
        print(f"Holder Name    : {self._holder_name}")
        print(f"Balance        : ₹{self._balance}")


# Inheritance: SavingsAccount inherits BankAccount
class SavingsAccount(BankAccount):
    """
    Savings account with interest feature
    Demonstrates inheritance and method overriding
    """

    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.04):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    # Method overriding
    def withdraw(self, amount):
        minimum_balance = 500
        if self._balance - amount >= minimum_balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn from savings account.")
        else:
            print("Withdrawal denied! Minimum balance ₹500 required.")

    # Add interest
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest ₹{interest:.2f} added.")


# -------------------------------
# Simulating real bank operations
# -------------------------------
if __name__ == "__main__":

    # Creating multiple objects
    account1 = BankAccount(101, "Sanyam Jain", 5000)
    account2 = SavingsAccount(201, "Rahul Sharma", 8000)

    # Bank operations
    account1.deposit(2000)
    account1.withdraw(1500)
    account1.display_details()

    account2.withdraw(3000)
    account2.add_interest()
    account2.display_details()

    # Transfer simulation
    print("\n--- Transferring ₹1000 from Account1 to Account2 ---")
    if account1.get_balance() >= 1000:
        account1.withdraw(1000)
        account2.deposit(1000)

    account1.display_details()
    account2.display_details()
