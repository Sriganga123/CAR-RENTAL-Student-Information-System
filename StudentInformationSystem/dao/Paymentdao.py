from util.ConnUtil import dbConnection
from exception.PaymentValidationException import PaymentValidationException
class Payment(dbConnection):
    def validate_payment_data(self, Amount, PaymentDate):
        try:
            amount_float = float(Amount)
            if amount_float <= 0:
                raise PaymentValidationException("Invalid payment amount. Amount must be greater than 0.")
            if not PaymentDate:
                raise PaymentValidationException("Payment date is required.")
        except ValueError:
            raise PaymentValidationException("Invalid payment amount format. Amount must be a valid number.")

    def AddPayment(self,PaymentID,StudentID,Amount,PaymentDate):
        try:
            self.validate_payment_data(Amount, PaymentDate)
            self.PaymentID=PaymentID
            self.StudentID=StudentID
            self.Amount=Amount
            self.PaymentDate=PaymentDate
            self.open()
            insert_str='''insert into Payment(PaymentID,StudentID,Amount,PaymentDate) values(%s,%s,%s,%s)'''
            data=[(self.PaymentID,self.StudentID,self.Amount,self.PaymentDate)]
            self.stmt.executemany(insert_str,data)
            self.conn.commit()
        except PaymentValidationException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            self.close()
    def GetStudent(self):
        self.open()
        print("List of Students who made payments:")
        select_str='''select PaymentID,StudentID from Payment'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
    def GetPaymentAmount(self):
        self.open()
        print("Payment Amount")
        select_str='''select PaymentID,Amount from Payment'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
    def GetPaymentDate(self):
        self.open()
        print("Payment Dates")
        select_str='''select PaymentID,PaymentDate from Payment'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
