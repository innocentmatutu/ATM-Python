import json
from pathlib import Path
from Account import Account
class Bank:
    def __init__(self):
        self._accounts = {}
        self._data_file = Path(__file__).with_name("accounts.json")

    def add_account(self, account, account_number):
        if account_number in self._accounts:
            return False

        self._accounts[account_number] = account
        return True

    def find_account(self, account_number):
        return self._accounts.get(account_number)

    def save_accounts(self):
        saved_accounts = {}

        for account_number, account  in self._accounts.items():
            saved_accounts[account_number] = {
                "owner_name": account.owner_name,
                "balance": account.get_balance()
            }

        with self._data_file.open("w", encoding="UTF-8") as file:
            json.dump(saved_accounts, file, indent= 4)

    def load_accounts(self):
        if not self._data_file.exists():
            return False

        with self._data_file.open("r", encoding="UTF_8") as file:
            saved_accounts = json.load(file)

        for account_number, account_data in saved_accounts.items():
            account = Account(
                account_data["owner_name"],
                account_data["balance"]
            )
            self._accounts[account_number] = account

        return True