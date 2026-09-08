class BankAccount:
    def __init__(self,bal):
        self.__bal=bal
    def deposit(self,amount):
        if amount>0:
            self.__bal+=amount
            print("Amount deposited:",amount)
    def withdraw(self,amount):
        if amount>0 and amount<=self.__bal:
            self.__bal-=amount
            print("Amount withdrawn:",amount)
        else:
            print("Insufficient balance.")
    def check_balance(self):
        print("Current balance:",self.__bal)
acc1=BankAccount(1000)
acc1.deposit(274)
acc1.withdraw(376)
acc1.check_balance()
        