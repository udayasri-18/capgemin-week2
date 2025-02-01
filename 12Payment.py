class Payment:
    def process_payment(self):
        print("Payment is processed")
class Creditcardpayment(Payment):
    def process_payment(self):
        print("Payment is processed using credit card")
class Paypalpayment(Payment):
    def process_payment(self):
        print("Payment is processed through paypal")
class Bitcoinpayment(Payment):
    def process_payment(self):
        print("Payment is processed using bitcoin")

type=input("Enter the type of payment : ")
if type=='bitcoin':
    bitcoin=Bitcoinpayment()
    bitcoin.process_payment()
elif type=='paypal':
    paypal=Paypalpayment()
    paypal.process_payment()
elif type=='credit':
    credit=Creditcardpayment()
    credit.process_payment()
else:
    pay=Payment()
    pay.process_payment()