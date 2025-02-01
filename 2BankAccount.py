class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,depositmoney):
        self.balance=self.balance+depositmoney
        print("You've depoisted ",depositmoney)
        print("Your total balance is",self.balance)
    def withdraw(self,withdrawmoney):
        if withdrawmoney>self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-withdrawmoney
            print("You've withdrawn ",withdrawmoney)
            print("Your total balance is",self.balance)

bank=BankAccount(2000)
bank.withdraw(100)
bank.withdraw(11100)
bank.deposit(200)