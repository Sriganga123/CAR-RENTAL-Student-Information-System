from util.ConnUtil import dbConnection
from datetime import datetime

class Student1(dbConnection):
    def __init__(self, StudentID, FirstName, LastName, DateOfBirth, Email, PhoneNumber):
        super().__init__()
        self.StudentID = StudentID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.payment_history = []

    def MakePayment(self, PaymentID,amount, paymentDate):
        data = (self.StudentID, PaymentID,amount, paymentDate)
        query = '''
            INSERT INTO Payment (StudentID, PaymentID,Amount, PaymentDate)
            VALUES (%s, %s, %s,%s)
        '''
        try:
            self.open()
            self.stmt.execute(query, data)
            self.conn.commit()
            print("Payment recorded successfully!")
        except Exception as e:
            print(f"Error recording payment: {e}")
        finally:
            self.close()

    def GetPaymentHistory(self):
        query = '''
            SELECT PaymentID, Amount, PaymentDate
            FROM Payment
            WHERE StudentID = %s
        '''
        try:
            self.open()
            self.stmt.execute(query, (self.StudentID,))
            payment_records = self.stmt.fetchall()
            return payment_records
        except Exception as e:
            print(f"Error retrieving payment history: {e}")
        finally:
            self.close()


