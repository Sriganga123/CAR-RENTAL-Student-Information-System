from util.ConnUtil import dbConnection
class PaymentRecord(dbConnection):
    def recordPayment(self):
        try:
            self.open()
            self.paymentID=int(input("Payment ID:"))
            self.leaseID=int(input("Lease ID"))
            self.paymentDate=input("Payment Date")
            self.amount=input("Amount")
            insert_str='''insert into Payment(paymentID,leaseID,paymentDate,amount)values(%s,%s,%s,%s)'''
            data=[(self.paymentID,self.leaseID,self.paymentDate,self.amount)]
            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            print("Payment Inserted successfully")
            self.close()
        except Exception as e:
            print(e)

