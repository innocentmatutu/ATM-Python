class Bank:
    def __init__(self):
        self._accounts = {}

    def add_account(self, account, account_number):
        if account_number in self._accounts:
            return False

        self._accounts[account_number] = account
        return True

    def find_account(self, account_number):
        return self._accounts.get(account_number)