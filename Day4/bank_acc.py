class bankAccount:
    def __init__(self,bal=0):
        self.__balance=bal
    def deposit(self,amt):
        self.__balance+=amt 
        print("Amount added to account current balance: ",self.get_balance())
    def withdraw(self,amt):
        if(self.__balance<amt):
            print("Cannot deduct amount.\n Insufficient balance: ")
        else:
            self.__balance-=amt 
            print("Amount dedeucted.\n Available balance:",self.get_balance())
    def get_balance(self):
        return self.__balance
obj=bankAccount(4000)
dep=float(input("Enter amount to deposit: "))
obj.deposit(dep)
get=float(input("Enter amount to withdraw: "))
obj.withdraw(get)

print("Get balance:",obj.get_balance())