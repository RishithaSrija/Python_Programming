class payment:
    def pay(self,amount):
        self.amount=amount

class cashPay(payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} in cash")
class cardPay(payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} using credit/debit card")
class upiPay(payment):
     def pay(self,amount):
        print(f"Paid ₹{amount} using UPI")

payments = [cashPay(), cardPay(), upiPay()]
for p in payments:
    p.pay(1000)
