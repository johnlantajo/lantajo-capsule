class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private variable, cannot be accessed directly

    # Getter method to access the private balance
    def get_balance(self):
        return self.__balance

    # Setter method to modify the private balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

# Creating an instance of BankAccount
account = BankAccount("John Doe", 1000)

# Accessing balance using getter method
print(account.get_balance())  # Outputs: 1000

# Depositing money
account.deposit(500)  # Outputs: Deposited 500. New balance: 1500

# Trying to access the private variable directly will raise an error
# print(account.__balance)  # This will raise an AttributeError

# Withdrawing money
account.withdraw(200)  # Outputs: Withdrew 200. New balance: 1300
