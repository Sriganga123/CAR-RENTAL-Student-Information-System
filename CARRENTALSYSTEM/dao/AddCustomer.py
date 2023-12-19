from util.ConnUtil import dbConnection
class ADDCUSTOMER(dbConnection):
    def addCustomer(self, customerID,firstName,lastName,email,phoneNumber):
        try:
            data = [(customerID,firstName,lastName,email,phoneNumber)]
            create_str = '''INSERT INTO Customer(customerID,firstName,lastName,email,phoneNumber) VALUES(%s,%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(create_str, data)
            self.conn.commit()
            self.close()
            print("Inserted Successfully")
        except Exception as e:
            print(e)

