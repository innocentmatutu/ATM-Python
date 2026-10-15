from Account import Account
from ATM import ATM

def main():
    account = Account("Amina", 100.0)
    atm = ATM()
    atm.run(account)

if __name__ == "__main__":
    main()