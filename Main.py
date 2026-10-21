from Account import Account
from ATM import ATM
from Bank import Bank

def main():
    bank = Bank()
    bank.add_account(Account("Amina", 100.0),"1001")
    bank.add_account(Account("Brian", 250.0),"1002")
    
    atm = ATM()
    account = bank.find_account("1001")
    atm.run(account)

if __name__ == "__main__":
    main()