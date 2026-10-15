class ATM:
    def withdraw_from(self, account):
        try: 
            amount = float(input("Amount to withdraw: "))
        except ValueError: 
            print("Please enter a valid number.")
            return

        if account.withdraw(amount):
            print(f"Withdrawal successful. Balance: {account.get_balance()}")
        else:
            print("Withdrawal failed. Check the amount and available balance.")

    def deposit_to(self, account):
        try:
            amount = float(input("Amount to deposit: "))
        except ValueError:
            print("Please enter a valid number.")
            return
        if account.deposit(amount):
            print(f"Deposit successful. Balance: {account.get_balance()}")
        else:
            print("Deposit failed. The amount must be greater than zero.")

    def run(self, account):
        while True:
            print("\n1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                print(f"Balance: {account.get_balance()}")
            elif choice == "2":
                self.deposit_to(account)
            elif choice == "3":
                self.withdraw_from(account)
            elif choice == "4":
                print("Goodbye.")
                break
            else:
                print("Invalid option. Choose 1, 2, 3, or 4.")

               
