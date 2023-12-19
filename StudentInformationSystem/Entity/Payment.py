class Payment:
    def __init__(self,PaymentID,StudentID,Amount,PaymentDate):
        self.PaymentID=PaymentID
        self.StudentID=StudentID
        self.Amount=Amount
        self.PaymentDate=PaymentDate
        print(f"Payment ID:{self.PaymentID} \nStudent ID:{self.StudentID} \nAmount:{self.Amount} \nPayment Date:{self.PaymentDate}")

Payment(700,12,45000.00,'2023-09-08')