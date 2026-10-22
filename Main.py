from Account import Account
from ATM import ATM
from Bank import Bank

def main():
    bank = Bank()
    if not bank.load_accounts():
        bank.add_account(Account("Amina", 100.0),"1001")
        bank.add_account(Account("Brian", 250.0),"1002")
    
    atm = ATM()
    atm.run(bank)
    bank.save_accounts()

if __name__ == "__main__":
    main()