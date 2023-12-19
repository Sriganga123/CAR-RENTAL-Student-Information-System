class Payment:
    def __init__(self,paymentID,leaseID,paymentDate,amount):
        self.paymentID=paymentID
        self.leaseID=leaseID
        self.paymentDate=paymentDate
        self.amount=amount
        print(f'Payment ID={self.paymentID} \nLease ID={self.leaseID} \nPayment Date={self.paymentDate} \nAmount={self.amount}')

Payment(45,202,'23/02/2023',45000.00)