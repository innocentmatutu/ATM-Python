class ATM:
    def _read_amount(self,prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("please enter a valid number")
                
    def withdraw_from(self, account):
        amount = self._read_amount("Amount to withdraw: ")
        
        if account.withdraw(amount):
            print(f"Withdrawal successful. Balance: {account.get_balance()}")
        else:
            print("Withdrawal failed. Check the amount and available balance.")

    def deposit_to(self, account):
        amount = self._read_amount("Enter amount to deposit: ")

        if account.deposit(amount):
            print(f"Deposit successful. Balance: {account.get_balance()}")
        else:
            print("Deposit failed. The amount must be greater than zero.")

    def run(self, bank):
        while True:
            account_number = input("Enter your account number, or x to exit: ")
            if account_number.lower() == "x":
                print("Goodbye")
                return

            if not account_number.isdigit():
                print("Account number must contain digits only.")
                continue
        
            account = bank.find_account(account_number)
            if account is None:
                print("Account number not found.Please try again ")
            else:
                break

        attempts_remaining = 3
        authenticated = False

        while attempts_remaining > 0:
            entered_pin = input("Enter your pin number: ")

            if account.verify_pin(entered_pin):
                authenticated = True
                break

            attempts_remaining -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts_remaining}")

        if not authenticated:
            print("Too many incorrect PIN attempts.")
            return

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

               
