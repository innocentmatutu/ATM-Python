class Account:
    def __init__(self, owner_name, balance=0.0):
        if not owner_name or not owner_name.strip():
            raise ValueError("Owner name cannot be empty")

        if balance < 0:
            raise ValueError("Starting balance cannot be negative")

        self.owner_name = owner_name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True

